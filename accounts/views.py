from pprint import pprint
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, login as auth_login,
    login, logout)
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from accounts.forms import ActivationForm, AuthForm
from accounts.models import Tuser
from accounts.utils import generate_verification_code
from tossapp.sms_setting import sms


def activate(request, user):
    tuser = Tuser.objects.get(username=user)
    if request.method == "POST":
        form = ActivationForm(request.POST, user=tuser)
        if form.is_valid():
            tuser.is_active = True
            tuser.save()
            #Login user
            # user = authenticate(username=tuser.username, password=tuser.password)
            user = Tuser.objects.get(username=tuser.username)
            user.backend = 'accounts.backends.TauthBackend'
            # print settings.AUTHENTICATION_BACKENDS[0]
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('index'))
    else:
        form = ActivationForm()

    return render(request, "registration/activate.html",{'form':form,'user':tuser})


@sensitive_post_parameters()
@csrf_protect
@never_cache
def tlogin(request, template_name='registration/login.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           authentication_form=AuthForm,
           extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect('dashboard')
        elif '__all__' in form.errors.as_data():
            for error in form.errors.as_data()['__all__']:
                print("error",error.code)
                pprint(repr(error))
                if error.code == 'inactive':
                    messages.warning(request, 'Account is inactive')
                    tuser = form.user_cache
                    code = generate_verification_code()
                    tuser.verification_code = code
                    tuser.save()
                    sms.send("Tossapp verification code: " + str(tuser.verification_code), [tuser.phone_number])
                    return HttpResponseRedirect(reverse_lazy('activate', kwargs={'user': tuser.username}))
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


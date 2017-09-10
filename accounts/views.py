from braces.views import AnonymousRequiredMixin
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
    login, logout)
from pprint import pprint
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import deprecate_current_app
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url
import random

# Create your views here.
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import CreateView

from accounts.admin import UserCreationForm
from accounts.forms import ActivationForm, ChangeNumberForm, AuthForm
from accounts.models import Tuser
from accounts.sendSms import send_verification_sms
from accounts.utils import generate_verification_code


# @login_required
# def index(request):
#     return render(request,'registration/index.html')

def activate(request,user):
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


class RegisterView(AnonymousRequiredMixin,CreateView):
    template_name='registration/register.html'
    authenticated_redirect_url = reverse_lazy("index")
    form_class = UserCreationForm
    # success_url=reverse_lazy('activate')

    def get_initial(self):
        return {'referrer_username': self.kwargs.get('username','')}

    def get_success_url(self):
        tuser = self.object
        print "In register view"
        pprint(tuser)
        code = generate_verification_code()
        tuser.verification_code = code
        tuser.save()
        print("Username: "+tuser.username)
        print("Verification Code: "+tuser.verification_code)
        # send_verification_sms(tuser.phone_number,tuser.verification_code)
        return reverse_lazy('activate', kwargs={'user': tuser.username})

def change_number(request,user):
    tuser = Tuser.objects.get(username=user)
    if request.method == "POST":
        form = ChangeNumberForm(request.POST)
        if form.is_valid():
            # pprint(repr(form.cleaned_data))
            tuser.phone_number = form.cleaned_data['phone_number']
            code = generate_verification_code()
            tuser.verification_code = code
            tuser.save()
            # send_verification_sms(tuser.phone_number,tuser.verification_code)
            return HttpResponseRedirect(reverse_lazy('activate', kwargs={'user': tuser.username}))
    else:
        form = ChangeNumberForm()

    return render(request, "registration/change_number.html",{'form':form,'user':tuser.username})

@deprecate_current_app
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
                    # send_verification_sms(tuser.phone_number,tuser.verification_code)
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
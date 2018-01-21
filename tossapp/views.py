from pprint import pprint

from cbvtoolkit.views import MultiFormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, PageNotAnInteger
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, FormView
from django.db.models import Count

from accounts.models import Tuser
from tossapp.forms import ChangePasswordForm, ChangeUsernameForm, ContactForm, ChangeProfileForm, ChangeDpForm,\
DepoForm
from tossapp.models import Notification, Game, Game_stat, Transaction, Faq


def index(request):
    context = RequestContext(request)
    if request.user.is_authenticated:
        page = 'Dashboard'
    else:
        page = ''
    page_brief = 'dashboard & statistics'
    if request.user.is_authenticated:
        return render(request, 'tossapp/index.html', locals(), contact)
    else:
        return render(request, 'dashboard/index.html', locals(), context)


@login_required
def dashboard(request):
    context = RequestContext(request)
    page = 'Dashboard'
    page_brief = 'dashboard & statistics'
    return render(request,'tossapp/index.html', locals(), context)


@csrf_protect
def contact(request, template_name='tossapp/contact_us.html'):
    context = RequestContext(request)
    page_title = 'Contact Us | Tossapp'
    page_intro = 'Contact Us'
    if request.method == "POST":
        myqn_form = ContactForm(request.POST)
        myqn_form.save()
        messages.success(request, 'Successfully submitted your Message ')
        return HttpResponseRedirect(reverse_lazy('contact'))
    else:
        myqn_form = ContactForm()
    return render(request, template_name, locals(), context)


class faq(ListView):
    page_title = 'FAQ | Tossapp'
    page_intro = 'Frequently Asked Questions'
    template_name = 'tossapp/faq.html'
    context_object_name = 'faq_list'
    model = Faq
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(faq, self).get_context_data(**kwargs)
        context.update({'page_title': self.page_title, 'page_intro': self.page_intro})
        return context


def how_it_works(request):
    return render(request, 'tossapp/how_it_works.html')


def about_us(request):
    context = RequestContext(request)
    page_title = 'About Us | Tossapp'
    page_intro = 'About Us'
    return render(request, 'tossapp/abouts_us.html', locals(), context)


class dashboard_notifications(LoginRequiredMixin, ListView):
    page = 'Notifications'
    page_brief = 'Notification & updates'
    template_name = 'dashboard/notifications.html'
    context_object_name = 'notification_list'
    paginate_by = 10

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).all()[:30]

    def get_context_data(self, **kwargs):
        notification_count = Notification.objects.filter(user=self.request.user, seen_status=False).count()
        context = super(dashboard_notifications, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief, 'notification_count':notification_count})
        return context


@login_required
def notification_status(request, n_id):
    if request.user.is_authenticated:
        n_s = get_object_or_404(Notification, pk=n_id)
        n_s.seen_status = True
        n_s.save()
        return HttpResponseRedirect(reverse_lazy('dashboard_notifications'))
    else:
        raise Http404


class dashboard_games(LoginRequiredMixin, ListView):
    page = 'All Games'
    page_brief = 'Choose a game you want to play'
    template_name = 'dashboard/games.html'
    context_object_name = 'game_list'
    model = Game

    def get_context_data(self, **kwargs):
        context = super(dashboard_games, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context


class dashboard_games_history(LoginRequiredMixin, ListView):
    page = 'Games History'
    page_brief = 'Games Statistics'
    template_name = 'dashboard/games_history.html'
    context_object_name = 'game_stat_list'

    def get_queryset(self):
        return Game_stat.objects.filter(user=self.request.user)[:15]

    def get_context_data(self, **kwargs):
        context = super(dashboard_games_history, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context


class dashboard_transactions(LoginRequiredMixin, ListView):
    page = 'Transactions'
    template_name = 'dashboard/transactions.html'
    context_object_name = 'transaction_list'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(dashboard_transactions, self).get_context_data(**kwargs)
        context.update({'page': self.page})
        return context


class dashboard_payments_withdraw(LoginRequiredMixin, FormView):
    page = 'Withdraw Funds'
    page_brief = 'Get your Funds onto your prefered Account instantly '
    template_name = 'dashboard/payments_withdraw.html'
    form_class = DepoForm
    success_url = reverse_lazy('dashboard_payments_withdraw')

    def get_context_data(self, **kwargs):
        context = super(dashboard_payments_withdraw, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context


class dashboard_payments_deposit(LoginRequiredMixin, TemplateView):
    page = 'Deposit Funds'
    page_brief = 'Deposit & Play'
    template_name = 'dashboard/payments_deposit.html'

    def get_context_data(self, **kwargs):
        context = super(dashboard_payments_deposit, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context


class dashboard_referrals(LoginRequiredMixin, ListView):
    page = 'Referrals'
    page_brief = 'Tell some of your friends and earn more Money'
    template_name = 'dashboard/referrals.html'
    players = Tuser.objects.all().annotate(num_refferals=Count('referrals')).order_by('-num_refferals')[:10]
    context_object_name = 'referral_list'
    paginate_by = 10

    def get_queryset(self):
        return Tuser.objects.filter(referrer=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(dashboard_referrals, self).get_context_data(**kwargs)
        current_user = self.request.user.username
        context.update({'page': self.page, 'page_brief': self.page_brief, 'players':self.players, 'current_user':current_user})
        return context


class dashboard_account_profile(LoginRequiredMixin, UpdateView):
    page = 'Profile'
    page_brief = 'This is how your Profile Looks Like'
    template_name = 'dashboard/account_profile.html'
    context_object_name = 'tuser'
    form_class = ChangeDpForm
    success_url = reverse_lazy('dashboard_account_profile')

    def get_object(self, queryset=None):
        user = get_object_or_404(Tuser, pk=self.request.user.id)
        user.games_played = Game_stat.objects.filter(user=self.request.user).count()
        user.games_won = Game_stat.objects.filter(user=self.request.user,status=Game_stat.WIN).count()
        user.games_lost = Game_stat.objects.filter(user=self.request.user,status=Game_stat.LOSE).count()
        user.referral_count = self.request.user.referrals.count()
        return user

    def get_context_data(self, **kwargs):
        context = super(dashboard_account_profile, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context


class dashboard_account_settings(LoginRequiredMixin, MultiFormView):
    page = 'Settings'
    page_brief = 'Customize your Account your way'
    template_name = 'dashboard/account_settings.html'
    success_url = reverse_lazy('dashboard_account_settings')
    forms = (ChangeUsernameForm, ChangePasswordForm)

    def get_context_data(self, **kwargs):
        context = super(dashboard_account_settings, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context


    # def get_success_url(self):
    #     pprint(self)
    # def get_changepasswordform_instance(self):
    #     return ChangePasswordForm(user=self.request.user)

    def changeusernameform_valid(self, form):
        tuser = Tuser.objects.get(username=form.cleaned_data['current_username'])
        tuser.username = form.cleaned_data['new_username']
        tuser.save()
        messages.success(self.request, 'successfully updated your Username')
        Notification.objects.create(user=self.request.user, title='Successfully updated Username', description='Username has been changed', type=0)
        return

    def changepasswordform_valid(self, form):
        tuser = Tuser.objects.get(pk=self.request.user.id)
        tuser.set_password(form.cleaned_data['new_password'])
        tuser.save()
        messages.success(self.request, 'successfully updated your Password')
        Notification.objects.create(user=self.request.user, title='Password', description='Password has been changed', type=0)
        return

    def post(self, request, *args, **kwargs):
        """
        Processes a single form, requires a form identifier in the params named `form_name`.
        """
        form_name = request.POST.get('form_name')
        if form_name not in self._forms_dict:
            return HttpResponseForbidden()

        form = self._forms_dict[form_name](request.POST, request.FILES, user=self.request.user)
        if form.is_valid():
            return self._form_valid(form_name, form)
        else:
            kwargs = {
                form_name: form,
            }
            messages.error(self.request, 'Something went wrong during filling')
            return self.render_to_response(self.get_context_data(**kwargs))


@login_required
def edit_profile(request):
    context = RequestContext(request)
    page = 'Edit Your Profile'
    page_brief = 'edit your profile by filling the form below.'
    if request.method == 'POST':
        form = ChangeProfileForm(data=request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse_lazy('dashboard_account_profile'))
    else:
        form = ChangeProfileForm()
    return render(request, 'dashboard/edit_user_settings.html', locals(), context)


class Latest_events(TemplateView):
    page_title = 'Latest events| Tossapp'
    page_intro = 'Latest events'
    template_name = 'tossapp/latest_events.html'

    def get_context_data(self, **kwargs):
        context = super(Latest_events, self).get_context_data(**kwargs)
        context.update({'page_title': self.page_title, 'page_intro': self.page_intro})
        return context


class Toc(TemplateView):
    page_title = 'TAC| Tossapp'
    page_intro = 'Terms and Conditions'
    template_name = 'tossapp/toc.html'

    def get_context_data(self, **kwargs):
        context = super(Toc, self).get_context_data(**kwargs)
        context.update({'page_title': self.page_title, 'page_intro': self.page_intro})
        return context


class Privacy_policy(TemplateView):
    page_title = 'Privacy| Tossapp'
    page_intro = 'Our Privacy Policy'
    template_name = 'tossapp/privacy_p.html'

    def get_context_data(self, **kwargs):
        context = super(Privacy_policy, self).get_context_data(**kwargs)
        context.update({'page_title': self.page_title, 'page_intro': self.page_intro})
        return context


class Career(TemplateView):
    page_title = 'Career| Tossapp'
    page_intro = 'Careers'
    template_name = 'tossapp/career.html'

    def get_context_data(self, **kwargs):
        context = super(Career, self).get_context_data(**kwargs)
        context.update({'page_title': self.page_title, 'page_intro': self.page_intro})
        return context







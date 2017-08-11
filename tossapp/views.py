from pprint import pprint

from cbvtoolkit.views import MultiFormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView, DetailView
from accounts.models import Tuser
from tossapp.forms import ChangePasswordForm, ChangeUsernameForm
from tossapp.models import Notification, Game, Game_stat, Transaction, Contact_us, Faq


def index(request):
    if request.user.is_authenticated:
        page = 'Dashboard'
    else:
        page = ''
    page_brief = 'dashboard & statistics'
    if request.user.is_authenticated:
        return render(request, 'tossapp/index.html', locals(), contact)
    else:
        return render(request, 'dashboard/index.html')

@login_required
def dashboard(request):
    context = RequestContext(request)
    page = 'Dashboard'
    page_brief = 'dashboard & statistics'
    return render(request,'tossapp/index.html', locals(), context)

@csrf_protect
def contact(request, template_name='tossapp/contact_us.html'):
    context = RequestContext(request)
    page_title = 'ContactUs'
    if request.method == "POST":
        contact_name = request.POST['your_name']
        contact_email = request.POST['your_email']
        contact_subject = request.POST['your_subject']
        contact_message = request.POST['your_message']
        myqn = Contact_us.objects.create(your_name=contact_name, your_email=contact_email, your_subject=contact_subject, your_message=contact_message)
        myqn.save()
        messages.success(request, 'Successfully submitted your Message ')
        return HttpResponseRedirect('contact')
    return render(request, template_name, locals(), context)


def faq(request, template_name="tossapp/faq.html"):
    context = RequestContext(request)
    page = 'FAQ'
    faq_list = Faq.objects.all()
    paginator = Paginator(faq_list, 2)
    page1 = request.GET.get('page')
    try:
        faqs = paginator.page(page1)
    except PageNotAnInteger:
        faqs = paginator.page(paginator.num_pages)
    return render(request,'tossapp/faq.html', locals(), context)


def faq_detail(request, slug):
    faq = get_object_or_404(Faq, slug=slug)
    return render(request, 'tossapp/faq_detail.html', {'faq': faq})

"""
class dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    """

class dashboard_notifications(LoginRequiredMixin, ListView):
    page = 'Notifications'
    page_brief = 'Notification & updates'
    template_name = 'dashboard/notifications.html'
    context_object_name = 'notification_list'

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(dashboard_notifications, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context

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

class rock_paper_scissor(LoginRequiredMixin, TemplateView):
    page = 'Rock Paper Scissor'
    page_brief = "Wrap, Cut and Crash. That's all you have to do."
    template_name = 'games/rock-paper_scissor.html'

    def get_context_data(self, **kwargs):
        context = super(rock_paper_scissor, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context

class flip_coin(LoginRequiredMixin, TemplateView):
    page = 'Flip Coin'
    page_brief = "Find out how Lucky you can be, Just Flip."
    template_name = 'games/flip_coin.html'

    def get_context_data(self, **kwargs):
        context = super(flip_coin, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context

class money_slot(LoginRequiredMixin, TemplateView):
    page = 'Money Slot'
    page_brief = "Cheapest Money slot of all time. Try it Out."
    template_name = 'games/money_slot.html'

    def get_context_data(self, **kwargs):
        context = super(money_slot, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context

class dashboard_games_history(LoginRequiredMixin, ListView):
    page = 'Games History'
    page_brief = 'Games Statistics'
    template_name = 'dashboard/games_history.html'
    context_object_name = 'game_stat_list'

    def get_queryset(self):
        return Game_stat.objects.filter(user=self.request.user)

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

class dashboard_payments_withdraw(LoginRequiredMixin, TemplateView):
    page = 'Withdraw Funds'
    page_brief = 'Get your Funds onto your prefered Account instantly '
    template_name = 'dashboard/payments_withdraw.html'

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
    players = Tuser.objects.all().order_by('-rank')
    context_object_name = 'referral_list'

    def get_queryset(self):
        return Tuser.objects.filter(referrer=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(dashboard_referrals, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context


class dashboard_account_profile(LoginRequiredMixin, DetailView):
    page = 'Profile'
    page_brief = 'This is how your Profile Looks Like'
    template_name = 'dashboard/account_profile.html'
    context_object_name = 'tuser'

    def get_object(self):
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

    def changeusernameform_valid(self,form):
        tuser = Tuser.objects.get(username=form.cleaned_data['current_username'])
        tuser.username = form.cleaned_data['new_username']
        tuser.save()
        return

    def changepasswordform_valid(self,form):
        tuser = Tuser.objects.get(pk=self.request.user.id)
        tuser.set_password(form.cleaned_data['new_password'])
        tuser.save()
        return

    def post(self, request, *args, **kwargs):
        """
        Processes a single form, requires a form identifier in the params named `form_name`.
        """
        form_name = request.POST.get('form_name')
        if form_name not in self._forms_dict:
            return HttpResponseForbidden()

        form = self._forms_dict[form_name](request.POST, request.FILES,user=self.request.user)
        if form.is_valid():
            return self._form_valid(form_name, form)
        else:
            kwargs = {
                form_name: form,
            }
            return self.render_to_response(self.get_context_data(**kwargs))




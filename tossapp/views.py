from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, ListView
from tossapp.forms import ContactForm
from tossapp.models import Notification, Faq


def index(request):
    context = RequestContext(request)
    page_brief = 'dashboard & statistics'

    return render(request, 'tossapp/index.html', locals(), context)


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


@login_required
def notification_status(request, n_id):
    if request.user.is_authenticated:
        n_s = get_object_or_404(Notification, pk=n_id)
        n_s.seen_status = True
        n_s.save()
        return HttpResponseRedirect(reverse_lazy('dashboard_notifications'))
    else:
        raise Http404


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







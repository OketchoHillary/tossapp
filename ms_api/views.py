from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import RequestContext
from django.views.generic import TemplateView
from django.shortcuts import render

"""
class ms_api(LoginRequiredMixin, TemplateView):
    page = 'Money Slot'
    page_brief = "Cheapest Money slot of all time. Try it Out."
    template_name = 'games/ms_api.html'

    def get_context_data(self, **kwargs):
        context = super(ms_api, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context
        """


# Create your views here.
def money_slot(request):
    context = RequestContext(request)
    page = 'Money Slot'
    page_brief = "Cheapest Money slot of all time. Try it Out."
    return render(request, 'ms_api/index.html', locals(), context)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class compound_boxes(LoginRequiredMixin, TemplateView):
    page = 'Compound boxes'
    page_brief = ""
    template_name = 'games/compound_boxes.html'

    def get_context_data(self, **kwargs):
        context = super(compound_boxes, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context

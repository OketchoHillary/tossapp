from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class rock_paper_scissor(LoginRequiredMixin, TemplateView):
    page = 'Rock Paper Scissor'
    page_brief = "Wrap, Cut and Crash. That's all you have to do."
    template_name = 'games/rock-paper_scissor.html'

    def get_context_data(self, **kwargs):
        context = super(rock_paper_scissor, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context

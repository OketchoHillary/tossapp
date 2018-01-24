from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class flip_coin(LoginRequiredMixin, TemplateView):
    page = 'Flip Coin'
    page_brief = "Find out how Lucky you can be, Just Flip."
    template_name = 'games/flip_coin.html'

    def get_context_data(self, **kwargs):
        context = super(flip_coin, self).get_context_data(**kwargs)
        context.update({'page': self.page, 'page_brief': self.page_brief})
        return context

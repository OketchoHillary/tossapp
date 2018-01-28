from django.conf.urls import url

from rock_paper_scissor.views import rock_paper_scissor

urlpatterns = [
    url(r'^dashboard/rock-paper-scissor$', rock_paper_scissor, name='rock_paper_scissor'),

    ]
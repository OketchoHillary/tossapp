from django.conf.urls import url

from compound_box.views import compound_boxes

urlpatterns = [
    url(r'^dashboard/compound-box$', compound_boxes, name='compound_boxes'),
    ]
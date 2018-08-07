from django.conf.urls import re_path, include, url
from .views import OfferList
from . import views as api_view


urlpatterns = [
    url(r'^offers/$', OfferList.as_view(), name='offer-list'),
    url(r'^offers/(?P<pk>[^/.]+)/$', OfferList.as_view(), name='offer-detail'),
]
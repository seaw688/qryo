from django.conf.urls import re_path, include, url
from .views import ShopList
from . import views as api_view


urlpatterns = [
    url(r'^shops/$', ShopList.as_view(), name='shop-list'),
    url(r'^shops/(?P<pk>[^/.]+)/$', ShopList.as_view(), name='shop-detail'),
]
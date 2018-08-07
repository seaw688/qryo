from django.conf.urls import re_path, include, url
#from .views import UserViewSet, Logout
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import OfferList, ShopList #, UserLoginView, UserViewSet, , CategoryList
from django.contrib.auth import views
from . import views as api_view
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework_jwt.views import obtain_jwt_token


from .common.user.urls import urlpatterns as user_urls
from .common.category.urls import urlpatterns as category_urls
from .yomarket.offer.urls import urlpatterns as offer_urls
from .yomarket.shop.urls import urlpatterns as shop_urls
from .yomarket.qrcode.urls import urlpatterns as qr_urls

urlpatterns = [
    # url(r'^user/login/$', UserLoginView.as_view(), login_kwargs, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    #url(r'^api-token-auth/', obtain_jwt_token),

    #url(r'^account/', include('account.urls')),

    #url(r'^categories/$', CategoryList.as_view()),
    # url(r'^offers/$', OfferList.as_view(), name='offer-list'),
    # url(r'^offers/(?P<pk>[^/.]+)/$', OfferList.as_view(), name='offer-detail'),
    # url(r'^shops/$', ShopList.as_view(), name='shop-list'),
    # url(r'^shops/(?P<pk>[^/.]+)/$', ShopList.as_view(), name='shop-detail'),
]


urlpatterns = urlpatterns + user_urls + category_urls + offer_urls + shop_urls + qr_urls




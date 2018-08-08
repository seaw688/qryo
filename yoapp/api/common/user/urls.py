from django.conf.urls import re_path, include, url
from rest_framework import routers
from .views import UserViewSet, Logout ,google_oauth
from . import views as api_view



router = routers.DefaultRouter()
router.include_format_suffixes = False
router.register(r'users', UserViewSet, base_name='UserView')

urlpatterns = router.urls

urlpatterns += [
    url(r'^registration/$', api_view.register_view, name='user_registration'),
    url(r'^login/$', api_view.login_view, name='user_login'),
    url(r'^logout/', Logout.as_view(), name='user_logout'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^google/$', google_oauth, name='google_login'),

]
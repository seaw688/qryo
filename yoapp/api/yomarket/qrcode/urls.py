from django.conf.urls import  url

from api.yomarket.qrcode.views import qr_checkout, offer_make_qr

urlpatterns = [
    url(r'^qr/checkout/(?P<uuid>.{0,50})$',qr_checkout),
    url(r'^qr/make_qr/(?P<offer_id>\d{0,50})$', offer_make_qr)

]
from django.contrib import admin
from .models import Shop, Offer
from yomarket.models import QRcoupon

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'shop', 'category', 'price', 'discount', 'discount_type', 'available')
    list_filter = ('shop', 'category', 'discount_type', 'available')
    search_fields = ('title', 'shop', 'category')
    date_hierarchy = 'created'
    ordering = ['updated', 'available']


admin.site.register(Shop)
admin.site.register(Offer, OfferAdmin)
admin.site.register(QRcoupon)

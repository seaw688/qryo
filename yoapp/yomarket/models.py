from django.db import models
from django.conf import settings
from django.apps import apps
#from ..common import Category, User


DISCOUNT_TYPES = (
    ('ABSOLUTE', 'ABSOLUTE'),
    ('PERCENT', 'PERCENT'),
)


class Shop(models.Model):
    user = models.ForeignKey('common.User', related_name='shops_user',
                             on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    # def __unicode__(self):
    #     return self.title


class Offer(models.Model):
    category = models.ForeignKey('common.Category', related_name='offers_from_category',
                                 on_delete=models.DO_NOTHING)
    shop = models.ForeignKey(Shop, related_name='shop_offer',
                             on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='offers/%Y/%m/%d', blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=50, choices=DISCOUNT_TYPES, default='ABSOLUTE')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    code_data = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ('title',)
        #index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    pass



class QRcoupon(models.Model):
    uuid = models.CharField(max_length=36, unique=True)
    short_uuid=models.CharField(max_length=8,unique=True)
    available = models.BooleanField(default=True)
    expiry_date = models.DateTimeField()
    date_created = models.DateTimeField(('date joined'), auto_now_add=True)

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    offer=models.ForeignKey(Offer, related_name='offer',on_delete=models.CASCADE,null=True)

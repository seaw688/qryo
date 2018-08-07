import sys
sys.path.append("..")

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import authenticate
from django.apps import apps
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.password_validation import validate_password as vp
#from common.utils import ROLES, DEFAULT_USER_ROLE


UserModel = get_user_model()
CategoryModel = apps.get_model('common', 'Category')
OfferModel = apps.get_model('yomarket', 'Offer')
ShopModel = apps.get_model('yomarket', 'Shop')



# class OfferSerializer(serializers.ModelSerializer):
#     shop = serializers.StringRelatedField()
#     category = serializers.StringRelatedField()
#
#     class Meta:
#         model = OfferModel
#         fields = ('id', 'category', 'shop', 'title', 'image', 'short_description',
#                   'description', 'price', 'discount', 'discount_type', 'code_data')



# class ShopSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField()
#
#     class Meta:
#         model = ShopModel
#         fields = ('id', 'title', 'address', 'user')
#
#     # def to_representation(self, instance):
#     #     # instance is the model object. create the custom json format by accessing instance attributes normaly
#     #     # and return it
#     #     identifiers = dict()
#     #     identifiers['id'] = instance.id
#     #     identifiers['title'] = instance.title
#     #
#     #     representation = {
#     #         'identifiers': identifiers,
#     #         #'user_id': instance.user_id,
#     #         'address': instance.address
#     #     }
#     #
#     #     return representation


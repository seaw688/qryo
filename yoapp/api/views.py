from django.shortcuts import render, HttpResponseRedirect
from django.apps import apps
from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import get_object_or_404
#from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView


from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, mixins
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from django.apps import apps

#from .serializers import ShopSerializer #, \ CategorySerializer, OfferSerializer,
    #CustomUserSerializer, LoginSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework.pagination import LimitOffsetPagination

from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from django.core.exceptions import ObjectDoesNotExist

from rest_auth.models import TokenModel
from rest_auth.app_settings import create_token



UserModel = get_user_model()
CategoryModel = apps.get_model('common', 'Category')
OfferModel = apps.get_model('yomarket', 'Offer')
ShopModel = apps.get_model('yomarket', 'Shop')


def custom_api_response(serializer=None, content=None, errors=None, metadata=None):
    if content:
        response = {'metadata': {}, 'content': content}
        return response

    if errors:
        response = {'metadata': {}, 'errors': errors}
        return response

    if not hasattr(serializer, '_errors') or len(serializer._errors) == 0:
        if hasattr(serializer, 'data'):
            response = {'metadata': {}, 'content': serializer.data}
        else:
            response = {'metadata': {}, 'content': 'unknown'}
    else:
        response = {'metadata': {}, 'errors': serializer._errors}
    return response


# class OfferList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request, format=None, pk=None):
#         offers = OfferModel.objects.all()
#         if pk is not None:
#             #offers = get_object_or_404(offers, pk=pk)
#             offers = OfferModel.objects.filter(pk=pk).all()
#             serializer = OfferSerializer(offers)
#         else:
#             serializer = OfferSerializer(offers, many=True)
#         response = Response(custom_api_response(serializer), status=status.HTTP_200_OK)
#         #return Response(serializer.data)
#         return response


# class ShopList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request, format=None):
#         shops = ShopModel.objects.all()
#         serializer = ShopSerializer(shops, many=True)
#         #return Response(serializer.data)
#         return Response(custom_api_response(serializer), status=status.HTTP_200_OK)



# # class UserDetail(viewsets.ModelViewSet):
#     """
#     API endpoint that represents a single user.
#     """
#     #model = User
#     #queryset = User.objects.filter(id = pk).first()
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer
#
#
#
# class UserCreateView(generics.CreateAPIView):
#     serializer_class = serializers.UserSerializer



#@method_decorator(csrf_exempt, name='dispatch')
# class UserLoginView(LoginView):
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         print (request, *args, **kwargs)
#         print ('UserLoginView')
#         return super(UserLoginView, self).dispatch(request, *args, **kwargs)

    # print('here')
    # pass








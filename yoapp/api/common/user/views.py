from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_auth.models import TokenModel
from rest_auth.app_settings import create_token

from ...views import custom_api_response
from .serializers import CustomUserSerializer, LoginSerializer


UserModel = get_user_model()


class Logout(APIView):
    #queryset = UserModel.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        django_logout(request)

        content = {"detail": "Successfully user logged out"}
        return Response(custom_api_response(None, content), status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    #queryset = UserModel.objects.filter(role='CUSTOMER').all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        #queryset = UserModel.objects.filter(role='CUSTOMER').all()
        #user = get_object_or_404(queryset, pk=pk)
        user = UserModel.objects.filter(role='CUSTOMER', pk=pk).all()
        serializer = CustomUserSerializer(user, many=True)
        #serializer.is_valid()
        response = Response(custom_api_response(serializer), status=status.HTTP_200_OK)
        return response

    def list(self, request, *args, **kwargs):
        users = UserModel.objects.filter(role='CUSTOMER').all()

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #serializer = self.get_serializer(queryset, many=True)
        serializer = CustomUserSerializer(users, many=True)

        return Response(custom_api_response(serializer), status=status.HTTP_200_OK)

    #@csrf_exempt
    # def create(self, validated_data):
    #     self.permission_classes = (AllowAny,)
    #     #print (self)
    #     user = super(UserViewSet, self).create(validated_data)
    #     #user.set_password(validated_data['password'])
    #     print (user)
    #     user.save()
    #     return user


@api_view(['POST'])
@permission_classes(())
def register_view(request):
    # обработчик регистрации
    if request.user.is_authenticated == True:
        error = {"detail": "You must have to log out first"}
        return Response(custom_api_response(errors=error), status=status.HTTP_400_BAD_REQUEST)

    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(custom_api_response(serializer), status=status.HTTP_201_CREATED)
    else:
        return Response(custom_api_response(serializer), status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes(())
def login_view(request):
    #serializer = AuthTokenSerializer(data=request.data)
    if request.user.is_authenticated == True:
        error = {"detail": "You must have to log out first"}
        return Response(custom_api_response(errors=error), status=status.HTTP_400_BAD_REQUEST)

    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token = create_token(TokenModel, user, serializer)
        #token = Token.objects.get(user=user)
        django_login(request, user)
        content = {'token': token.key, 'email': user.email, 'id': user.id}
        return Response(custom_api_response(serializer, content), status=status.HTTP_200_OK)
        #return Response({'token': token.key, 'username': user.username, 'id': user.id})
    else:
        return Response(custom_api_response(serializer), status=status.HTTP_400_BAD_REQUEST)




import httplib2
from googleapiclient.discovery import build
from oauth2client.client import AccessTokenCredentials
@api_view(['POST'])
@permission_classes(())
def google_oauth(request):
    if request.user.is_authenticated:
        return Response({"detail": "You must have to log out first"})

    access_token = request.data['access_token']
    credentials = AccessTokenCredentials(access_token,'my-user-agent/1.0')
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build('plus', 'v1', http=http)
    result=service.people().get(userId='me').execute()

    email=result['emails'][0]['value']
    gender=result['gender']
    first_name=result['name']['givenName']
    last_name=result['name']['familyName']
    photo=result['image']['url']

    def create_login_token(user):
        serializer = LoginSerializer()
        token = create_token(TokenModel, user, serializer)
        return token

    try:
        user=UserModel.objects.get(email=email)
    except UserModel.DoesNotExist:
        user=UserModel(email=email,last_name=last_name,first_name=first_name)
        user.set_password('password')
        user.save()

    token=create_login_token(user)

    return Response({'token':token.key})

from django.apps import apps
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from ...views import custom_api_response
from .serializers import ShopSerializer


ShopModel = apps.get_model('yomarket', 'Shop')


class ShopList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        shops = ShopModel.objects.all()
        serializer = ShopSerializer(shops, many=True)
        #return Response(serializer.data)
        return Response(custom_api_response(serializer), status=status.HTTP_200_OK)


from django.apps import apps
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from ...views import custom_api_response
from .serializers import OfferSerializer


OfferModel = apps.get_model('yomarket', 'Offer')


class OfferList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None, pk=None):
        #offers = OfferModel.objects.all()  # .filter(category__category_name__exact='cat two')
        offers = OfferModel.objects.all() # .filter(category_id=2)
        if pk is not None:
            #offers = get_object_or_404(offers, pk=pk)
            offers = OfferModel.objects.filter(pk=pk).all()
            serializer = OfferSerializer(offers, many=True)
        else:
            category_id = self.request.query_params.get('category_id', None)
            if category_id is not None:
                #from .serializers import catedory_id_validate
                #catedory_id_validate(category_id)
                offers = offers.filter(category_id=category_id)

            shop_id = self.request.query_params.get('shop_id', None)
            if shop_id is not None:
                offers = offers.filter(shop_id=shop_id)

            serializer = OfferSerializer(offers, many=True)

        response = Response(custom_api_response(serializer), status=status.HTTP_200_OK)
        #return Response(serializer.data)
        return response
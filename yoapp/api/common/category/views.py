from django.apps import apps
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from ...views import custom_api_response
from .serializers import CategorySerializer


CategoryModel = apps.get_model('common', 'Category')


class CategoryList(APIView):
    permission_classes = (AllowAny,)
    #pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    #print (pagination_class)


    def get(self, request, format=None):
        #paginator = LimitOffsetPagination()
        categories = CategoryModel.objects.all()
        #result_page = paginator.paginate_queryset(categories, request)
        serializer = CategorySerializer(categories, many=True) # , context={'request': request}
        #response = Response(serializer.data, status=status.HTTP_200_OK)
        response = Response(custom_api_response(serializer), status=status.HTTP_200_OK)
        return response

    # def get(self, request, pk, format=None):
    #     # user = request.user
    #     event = Event.objects.get(pk=pk)
    #     news = event.get_news_items().all()
    #     paginator = LimitOffsetPagination()
    #     result_page = paginator.paginate_queryset(news, request)
    #     serializer = NewsItemSerializer(result_page, many=True, context={'request': request})
    #     response = Response(serializer.data, status=status.HTTP_200_OK)
    #     return response
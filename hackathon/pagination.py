from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from main.models import Article
from . import serializers


class StandardResultPagination(PageNumberPagination):
    page_size = 100
    page_query_param = 'page_size'
    max_page_size = 1000


class ProductListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_class = (permissions.IsAuthenticated, )
    pagination_class = StandardResultPagination

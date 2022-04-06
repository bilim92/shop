from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated

from applications.product.models import Product
from applications.product.serializers import ProductSerializer


class ListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class DeleteUpdateRetriveView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

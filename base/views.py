from django.shortcuts import render
from .models import ProductType
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductTypeSerializer

# Create your views here.

class  ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

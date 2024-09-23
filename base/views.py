from django.shortcuts import render
from .models import ProductType,Product
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .serializers import ProductTypeSerializer,ProductSerializer
from rest_framework.response import Response
# Create your views here.

class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    
    
class ProductApiView(GenericAPIView):
    def get(self,request):
       product_objs = Product.objects.all()
       serializer = ProductSerializer(product_objs,many=True)
       return Response(serializer.data)
   
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response('Data Created')
        else:
           return Response(serializer.errors)
       
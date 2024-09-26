from django.shortcuts import render
from .models import ProductType,Product,Purchase,Department,Vendor,Sales,Customer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,ProductTypeSerializer,ProductSerializer,PurchaseSerializer,DepartmentSerializer,VendorSerializer,SalesSerializer,CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Registered Successfully')
    else:
        return Response(serializer.errors)

class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    
    
class ProductApiView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
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

class ProductDetailApiView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self,request,pk):
        try:
           product_obj = Product.objects.get(id=pk)
        except:
            return Response('Data Not Found!')
        serializer = ProductSerializer(product_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
           product_obj = Product.objects.get(id=pk)
        except:
            return Response('Data Not Found!')
        
        serializer = ProductSerializer(product_obj,data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response('Data Updated!')
        else:
            return Response(serializer.errors)
    
     
    def delete(self,request,pk):
      
        try:
           product_obj = Product.objects.get(id=pk)
          
        except:
            return Response('Data Not Found!')
        product_obj.delete()
        return Response('Data Deleted!')
        
class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class DepartmentApiView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class VendorApiView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class SalesApiView(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class CustomerApiView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
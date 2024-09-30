from rest_framework.serializers import ModelSerializer
from .models import User,ProductType,Product,Purchase,Department,Vendor,Sales,Customer
from django.contrib.auth.models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =  ['full_name','email','password','image','phone_number','groups']

    
class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
        
    
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
 
        
class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
 
        
class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
 
        
class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
 
        
class SalesSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
 
        
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        

        
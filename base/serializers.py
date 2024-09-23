from rest_framework.serializers import ModelSerializer
from .models import ProductType,Product

class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
        
    
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
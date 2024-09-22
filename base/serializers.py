from rest_framework.serializers import ModelSerializer
from .models import ProductType

class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
        
    
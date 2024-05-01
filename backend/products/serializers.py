from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields=[
            'title','sale_price','price','content','my_discount',
        ]
        
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return  None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()
        
#multiple serializers for exact same model
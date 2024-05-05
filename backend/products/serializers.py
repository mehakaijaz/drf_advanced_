from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators 


class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    #perferred method
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',
                                             lookup_field='pk')
    email=serializers.EmailField(write_only=True)
    title=serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title])
    name=serializers.CharField(source='title',read_only=True)
    class Meta:
        model=Product
        fields=[
            'name',
            'title','sale_price','price','content','my_discount','url','edit_url',"pk","email",
        ]
      
    #custom validations
    # def validate_title(self,value):
    #     request=request.context.get('request')
    #     user=request.user
    #     qs=Product.objects.filter(user=user,title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
        
    #     return value
        
      
    # def get_url(self,obj):
    #    # return f'/api/products/{obj.pk}/'
    #     request=self.context.get('request')#self.request
    #     if request is None:
    #         return None
    #     return reverse("product-detail",kwargs={"pk":obj.pk},request=request)  
    
    
    #exAMple
    # def create(self,validated_data):
    #     #return Product.objects.create(**validated_data)#unpacking data
    #     #email=validated_data.pop("email")
    #     obj= super().create(validated_data)
    #     print(obj)
    #     return obj
    
    # def update(self,instance,validated_data):
    #     instance.title=validated_data.get("title")
    #     return instance
    
    def get_edit_url(self,obj):
    
        request=self.context.get('request')#self.request
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request) 
        
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return  None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()
    
        
#multiple serializers for exact same model
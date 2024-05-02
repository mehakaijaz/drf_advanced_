#viewsets and routers

from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    get->list->queryset
    get->retrieve-> product instance detail view 
    post->create->new instance
    put-> update
    patch->partial update
    delete->destroy
    all of these is similar to mixins methods
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'#default
    
class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    """
    get->list->queryset
    get->retrieve-> product instance detail view 
    working only on these two this time
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'#default
    
product_list_view=ProductGenericViewSet.as_view({"get":'list'})
product_detail_view=ProductGenericViewSet.as_view({"get":'retrieve'})
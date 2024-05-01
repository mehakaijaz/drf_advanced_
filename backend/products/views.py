from rest_framework import generics,mixins
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404  # also use from django.http import HTTP404


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        #print(serializer.validated_data)
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        #or None
        if content is None:
            content=title
        serializer.save(content=content)
        
        #send a django signals

      
    
product_list_create_view=ProductListCreateAPIView.as_view()

#generic views->CreateAPIView
"""class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        #print(serializer.validated_data)
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        #or None
        if content is None:
            content=title
        serializer.save(content=content)
        
        #send a django signals
product_create_view=ProductCreateAPIView.as_view()"""

#generic views-> RetrieveAPIView
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #look_up='pk'
    #Product.objects.get(pk="abc")
    
#generic views-> UpdateAPIView
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #look_up='pk'
    #Product.objects.get(pk="abc")
    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
    
#generic views-> DestroyAPIView
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    look_up='pk'
    #Product.objects.get(pk="abc")
    def perform_destroy(self,instance):
      #  instance
        super().perform_destroy(instance)
      
#NOT GONNA USE THIS METHOD INSTEAD LISTCREATEAPIVIEW 
#generic views-> ListAPIView
# class ProductListAPIView(generics.ListAPIView):
    # queryset=Product.objects.all()
    # serializer_class=ProductSerializer
    #look_up='pk'
    #Product.objects.get(pk="abc")

#mixins and a generic APIView
class ProductMixin(
    mixins.ListModelMixin, 
    generics.GenericAPIView):
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def post(self,request,*args, **kwargs):#http->get
        return self.list(request,*args, **kwargs)
    
    #def post(self,request,*args, **kwargs):#http->post
        return 

#the function based view
"""@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args, **kwargs):
    method=request.method
    
    if method=='GET':
        if pk is not None:
            #get data-> detail view
            #queryset=Product.objects.filter(pk=pk)
            if not queryset.exists():
                raise Http404  #(do like this or the given below)
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            
            return Response(data)
        else:
        #list view
            queryset=Product.objects.all()
            data=ProductSerializer(queryset,many=True).data
            return Response(data)
        
    if method=='POST':    
        #create an item
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance=serializer.save()
            title=serializer.validated_data.get("title")
            content=serializer.validated_data.get("content")
            #
            if content is None:
                content=title
            serializer.save(content=content)
            
            print(instance)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)"""
from rest_framework import generics,mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404  # also use from django.http import HTTP404
from api.permissions import IsStaffEditorPermission
from api.mixins import StaffEditorPermissionMixins
#authentications and permissions
class ProductListCreateAPIView(
    StaffEditorPermissionMixins,#no longer need to mention permissionclasses in code now, we can repeat this for each view or we ever needed in views
    generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #authentication_classes=[authentication.SessionAuthentication,
      #                      TokenAuthentication]
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly]#only list option will work not create ,update
    #permission_classes=[permissions.DjangoModelPermissions]#custom user permission jese h ye
    #permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]# agr default permissions set h 
    # toh ye mention krne ki jarurat nhi same for authclasses
    
    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        #print(serializer.validated_data)
        email=serializer.validated_data.pop("email")
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        print(email)
        #or None
        if content is None:
            content=title
        serializer.save(content=content)#similar to form.save()and model.save()
        
#         #send a django signals

      
    
product_list_create_view=ProductListCreateAPIView.as_view()

#generic views->CreateAPIView
# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#     permission_classes=[permissions.Is]
    
#     def perform_create(self, serializer):
#         #serializer.save(user=self.request.user)
#         #print(serializer.validated_data)
#         title=serializer.validated_data.get("title")
#         content=serializer.validated_data.get("content")
#         #or None
#         if content is None:
#             content=title
#         serializer.save(content=content)
        
#         #send a django signals
# product_create_view=ProductCreateAPIView.as_view()

#generic views-> RetrieveAPIView
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    look_up='pk'
    permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]
    #Product.objects.get(pk="abc")
    
#generic views-> UpdateAPIView
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[]#cutting off all permissions, same goes for authclasses as well
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
    permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]
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
#these are included in this view
#class ProductCreateAPIView(mixins.CreateModelMixin,generics.GenericAPIView):
   # pass

#mixins and a generic APIView
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,#CARE about lookup_field
    generics.GenericAPIView):
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk' #added cuz we are retrieving here
    
    def get(self,request,*args, **kwargs):#http->get
        print(args, kwargs)
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):#http->post
        return self.create(request,*args, **kwargs)

    def perform_create(self, serializer):
         #serializer.save(user=self.request.user)
        #print(serializer.validated_data)
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        #or None
        if content is None:
                content='this is the new single view'
                serializer.save(content=content)
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
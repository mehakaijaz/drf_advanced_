#from django.http import JsonResponse,HttpResponse 
from django.forms.models import model_to_dict
from rest_framework.response import Response
import json
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request,*args, **kwargs):
    
    #ingest data with drf views
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        #similar to
        #instance=forms.save()
        #print(serializer.data)
        print(instance)
        #data=serializer.data
        return Response(serializer.data)
    #return Response({"invalid": "not good data"}, status=400)

"""def api_home(request,*args, **kwargs):
    #request-> Http request-> from django
    #request.body
    body= request.body #btye string of json data
    #print(body)# iska o/p = b'{"hello world": "new there"}'
    print(request.GET)# url query parameters
    data={}
    try:
        data=json.loads(body)# string of json data -> python dict
    except:
        pass
    print(data)
    data['params']=dict(request.GET)
    data['headers']=dict(request.headers)
    data['content_type']=request.content_type
    model_data=Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data['id']=model_data.id
        data['title']=model_data.title
        data['content']=model_data.content
        data['price']=model_data.price 
        #in place of this now we can write this
        data=model_to_dict(model_data, fields=['id','title']) 
        #model instance (model_data)
        #turn python dict
        #return json to my client
    return JsonResponse(data)
    #return HttpResponse(data)# accepts string,if we run json error occurs"""

"""DRF API VIEW
    data=request.data
    instance=Product.objects.all().order_by("?").first()
    data={}
    if  instance:
        #data=model_to_dict( instance, fields=['id','title','price','sale_price']) 
        data=ProductSerializer(instance).data
    return Response(data)"""

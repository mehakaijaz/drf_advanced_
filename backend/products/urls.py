from django.urls import path
from . import views

urlpatterns = [
    
    #path('',views.product_list_create_view),
    path('<int:pk>/update/',views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/',views.ProductDeleteAPIView.as_view()),
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('',views.ProductMixin.as_view())
    #path('<int:pk>/',views.product_alt_view),
    #path('',views.product_alt_view),
    
]

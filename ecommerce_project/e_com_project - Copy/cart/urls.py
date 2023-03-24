from . import views
from django.urls import  path

app_name='cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('',views.cart_detail, name='cart_detail'),
]
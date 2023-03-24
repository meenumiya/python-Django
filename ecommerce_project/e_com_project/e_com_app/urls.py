from . import views
from django.urls import  path

app_name='e_com_app'

urlpatterns = [
    path('',views.allprocat, name='allprocat'),
    path('<slug:c_slug>/',views.allprocat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail, name='procatdetail'),


]
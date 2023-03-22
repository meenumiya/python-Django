from django.urls import path
from . import views
app_name='movieapp' #for name spacing
urlpatterns = [
    path('',views.index, name="index"),
    path('movies/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),


]
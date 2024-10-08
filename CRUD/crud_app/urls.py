
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.index,name='home'),
    path('delete_index/<id>/', views.delete_index,name='delete_index'),
    path('update_index/<id>/', views.update_index,name='update_index'),
    
]
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_rent/<str:pk>/', views.createRent, name="create_rent"),
    path('update_rent/<str:pk>/', views.updateRent, name="update_rent"),
    path('delete_rent/<str:pk>/', views.deleteRent, name="delete_rent"),
]
from django.urls import path
from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('home', views.home , name='home'),
    path('about/', views.about , name='about'),
    path('product/', views.product , name='product'),
    path('service/', views.service , name='service'),
    path('gallery/', views.gallery , name='gallery'),
    path('contact/', views.contact , name='contact'),
    path('contact_submit/', views.contact_submit , name='contact_submit'),
    path('order_details/', views.order_details , name='order_details'),
    
    
]
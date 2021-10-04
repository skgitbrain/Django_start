from django.urls import path
from mainapp.views import products, contact
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product'),
    path('category/<int:pk>/', mainapp.products, name='category'),

]



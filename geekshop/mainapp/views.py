from django.shortcuts import render

from mainapp.models import Product


def main(request):
    products = Product.objects.all()
    content = {'page_title': 'магазин', 'products': products}
    return render(request, 'mainapp/index.html', content)

def products(request):
    products_menu = ['все', 'дом','офис', 'модерн', 'классика']
    content = {'page_title': 'каталог', 'products_menu': products_menu}
    return render(request, 'mainapp/products.html', content)

def contact(request):
    content = {'page_title': 'контакты'}
    return render(request, 'mainapp/contact.html', content)




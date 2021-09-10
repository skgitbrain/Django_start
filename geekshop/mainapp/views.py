from django.shortcuts import render

def main(request):
    context = {'page_title': 'магазин'}
    return render(request, 'mainapp/index.html', context)

def products(request):
    products_menu = ['все', 'дом','офис', 'модерн', 'классика']
    context = {'page_title': 'каталог', 'products_menu': products_menu}
    return render(request, 'mainapp/products.html', context)

def contact(request):
    context = {'page_title': 'контакты'}
    return render(request, 'mainapp/contact.html', context)

def temp(request):
    return render(request, 'mainapp/temp1.html')


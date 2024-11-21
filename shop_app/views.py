from django.shortcuts import render, redirect
from .models import Product, CategoryProduct


# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        # Достаем все из БД
        products = Product.objects.all()
        categories = CategoryProduct.objects.all()
        # Передаем данные на фронт
        context = {'products': products, 'categories': categories}

        return render(request, 'index.html', context)
    print("sdfsd")
    return redirect('about')


def about(request):
    try:
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, "about.html")
    except:
        return render(request, 'about.html')


def category_page(request, pk):
    category = CategoryProduct.objects.get(id=pk)
    products = Product.objects.filter(product_category=category).all()
    # .first()//.all()
    # Передаем данные на фронт
    context = {'products': products, 'category': category}
    return render(request, 'category_product.html', context)


def product_page(request, pk):
    product = Product.objects.get(id=pk)
    # Передаем данные на фронт
    context = {'product': product}

    return render(request, 'product.html', context)

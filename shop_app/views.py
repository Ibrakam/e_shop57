from django.shortcuts import render, redirect
from .models import Product, CategoryProduct, UserCart
import telebot

bot = telebot.TeleBot("5605372341:AAHFL3_VEzjxLBSXbxYIuuIJLc-OSMP-1qA")


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


def add_product_to_cart(request, pk):
    if request.method == "POST":
        checker = Product.objects.get(id=pk)
        if checker.product_count >= int(request.POST.get('pr_count')):
            UserCart.objects.create(user_id=request.user.id,
                                    product=checker,
                                    product_count=int(request.POST.get('pr_count')))
            print("SUCCESS")
            return redirect('user_cart')
        else:
            print("ERROR")
            return redirect('home')


def user_cart(request):
    cart = UserCart.objects.filter(user_id=request.user.id).all()  # (UserCart(Product()))
    if request.method == "POST":
        main_text = 'У вас новый заказ'

        for i in cart:
            main_text += (f"\n Товар: {i.product.product_name}"
                          f"\n Кол-во: {i.product_count}"
                          f"\n ID-пользователя: {i.user_id}"
                          f"\n Цена: {i.product.product_cost}")
        bot.send_message(-4608156312, main_text)
        cart.delete()
        return redirect('home')
    else:
        return render(request, "user_cart.html", context={"cart": cart})

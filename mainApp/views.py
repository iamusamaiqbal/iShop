from django.contrib.auth import login as lu, authenticate, logout as lo
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db.models import Sum

from .models import *
from .form import RegisterForm


# Create your views here.

# recommendation
def recommend():
    product = Product.objects.all()

    return HttpResponse('hello')


def index(request):
    products = Product.objects.all().order_by("-product_Time")
    catg = SubCat.objects.all()

    if request.user.is_authenticated:
        current_user = request.user

        cart = Cart.objects.get(user=current_user.id)
        cart_id = cart.id

        item = CartItem.objects.filter(cart_id=cart_id)

        totalprice = item.aggregate(Sum('price')).get('price__sum')

        itemsinCart = item.count()
    else:
        itemsinCart = None
        totalprice = 0
        item = None

    dic = {
        'products': products,
        'catg': catg,
        'itemsinCart': itemsinCart,
        'totalprice': totalprice,
        'items': item
    }

    return render(request, 'index.html', dic)


def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            lu(request, user)
            return redirect('home')

        else:
            messages.info(request, "Incorrect username or password")

    return render(request, '')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                lu(request, user)
                return redirect('home')
                # messages.success(request, "Welcome " + username)
            else:
                messages.info(request, "Incorrect username or password")

    else:
        form = RegisterForm()
        return render(request, "", {'form': form})


def logout(request):
    lo(request)
    return redirect('home')


def product_detail(request, id=0):
    product = Product.objects.get(id=id)
    return render(request, 'shop-detail.html', {'product': product})


def add_to_cart(request, id=0):
    current_user = request.user
    if Cart.objects.filter(user_id=current_user.id):

        cart = Cart.objects.get(user=current_user.id)
        cart_id = cart.id

        product = Product.objects.get(id=id)

        item = CartItem.objects.filter(product_id=id)
        if item and product.product_Stock:

            item = CartItem.objects.get(product_id=id)
            item.quantity += 1
            item.price = item.quantity * product.product_Price
            item.cart_id = cart_id
            item.product_id = id
            item.save()

        else:
            item = CartItem(cart_id=cart_id, product_id=id, price=product.product_Price)
            item.save()

        messages.success(request, product.product_Name + " add to cart")
        return redirect('home')
    else:
        cart = Cart(user_id=request.user.id)
        cart.save()
        cart_id = cart.id

        product = Product.objects.get(id=id)

        item = CartItem(cart_id=cart_id, product_id=id, price=product.product_Price)
        item.save()

        messages.success(request, product.product_Name + " add to cart")
        return redirect('home')


def show_cart(request, id=0):
    cart = Cart.objects.get(user=id)
    cart_id = cart.id

    item = CartItem.objects.filter(cart_id=cart_id)

    totalprice = item.aggregate(Sum('price')).get('price__sum')

    dic = {
        'items': item,
        'total': totalprice
    }
    return render(request, 'cart.html', dic)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact-us.html')


def show_by_cat(request, id=0):
    product = Product.objects.filter(sub_cat=id)
    return render(request, 'products.html', {'products': product})

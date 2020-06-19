import requests
import base64
from django.shortcuts import render
from products.models import Comment, Order
import sqlite3
from django.contrib.auth.models import User



# Create your views here.
from products.models import Product

def product_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_index.html', context)

def product_detail(request, pk):
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        Comment(isim=request.POST['isim'],baslik = request.POST['baslik'], yorum=request.POST['yorum'],puan=int(request.POST['puan']),product_id = pk,user_id = user.id).save()
    comments = Comment.objects.filter(product_id = pk)
    comments.length = len(comments)
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
        'comments': comments[:5]
    }
    return render(request, 'product_detail.html', context)

def home_page(requests):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(requests, 'home_page.html', context)


def add_comment(requests):
    return render(requests, 'home_page.html', {})

def product_payment(request, pk):
    user = User.objects.get(username = request.user)
    Order(product_id=pk,user_id=user.id).save()
    return render(request, 'product_payment.html', {})


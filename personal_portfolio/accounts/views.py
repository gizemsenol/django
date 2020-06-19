from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Comment
from products.models import Order
# Create your views here.

#def indexView(request):
#    return render(request,'index.html')

@login_required 
def dashboardView(request):
    print()
    user = User.objects.get(username = request.user)
    comments = Comment.objects.filter(user_id = user.id)
    comments.length = len(comments) 
    #if request.method == 'POST':
    #    Order(product_id = pk,user_id = user.id).save()
    orders = Order.objects.filter(user_id = user.id)
    context = {
        'comments': comments,
        'orders':orders
    }
    return render(request,'dashboard.html', context)

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {"form":form})

def comment_view(request):
    user = User.objects.get(username = request.user)
    comments = Comment.objects.filter(user_id = user.id)
    comments.length = len(comments)
    context = {
        'comments': comments,
    }
    return render(request, 'comments.html', context)

def order_view(request):
    user = User.objects.get(username = request.user)
    orders = Order.objects.filter(user_id = user.id)
    orders.length = len(orders)
    context = {
        'orders': orders,
    }
    return render (request, 'orders.html', context)


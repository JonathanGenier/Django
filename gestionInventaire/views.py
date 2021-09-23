from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import (ProductForm, LoginForm, RegisterForm)
from .models import Product

# INDEX (HOME PAGE)
@login_required(login_url='login')
def indexView(request):
    items = Product.objects.all()
    return render(request, 'index.html', {'items': items})

# LOGIN PAGE
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = LoginForm()
            return render(request, "login.html", {'form': form})
    else:
        form = LoginForm()
        return render(request, "login.html", {'form': form})

# LOGOUT
@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('login')

# REGISTER PAGE
def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, "register.html", {'form': form})
    else:
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

# PRODUCT PAGE
@login_required(login_url='login')
def productView(request, pk):
    item = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'item': item})

# SALES PAGE
@login_required(login_url='login')
def salesView(request):
    items = []
    for item in Product.objects.all():
        if item.current_quantity < item.stock_quantity:
            items.append(item)

    return render(request, 'sales.html', {'items': items})

# ADD PAGE
@login_required(login_url='login')
def addView(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'add.html', {'form': form})

    else:
        form = ProductForm()
        return render(request, 'add.html', {'form': form})

# EDIT PAGE
@login_required(login_url='login')
def editView(request, pk): 
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'edit.html', {'form': form})
    else:
        form = ProductForm(instance=item)
        return render(request, 'edit.html', {'form': form})

# DELETE PAGE
@login_required(login_url='login')
def deleteView(request, pk):
    if request.method == "POST":
        Product.objects.filter(id=pk).delete()
        return redirect('/') 
    else:
        item = get_object_or_404(Product, pk=pk)
        return render(request, 'delete.html', {'item': item})

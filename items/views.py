from django.shortcuts import render, redirect
from items.models import Item
from items.forms import ItemForm
from django.contrib.auth import login, authenticate
from items.forms import SignUpFormAdmin, LoginFormAdmin
from django.contrib.auth.decorators import login_required
from items.models import Item

@login_required(login_url="admin_login")
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

@login_required(login_url="admin_login")
def home(request):
    items = Item.objects.all()
    return render(request, 'list_items.html', {'items': items})


def signup(request):
    if request.method == 'POST':
        form = SignUpFormAdmin(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = SignUpFormAdmin()
    return render(request, 'admin_signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginFormAdmin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = LoginFormAdmin()
    return render(request, 'admin_login.html', {'form': form})



# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from items.models import Item

# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# View to list all items
@login_required
def list_items(request):
    items = Item.objects.all()  # Get all items from the database
    return render(request, 'home.html', {'items': items})

# View to show details of a single item
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Get the item or 404 if not found
    return render(request, 'item_detail.html', {'item': item})
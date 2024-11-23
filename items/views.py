from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

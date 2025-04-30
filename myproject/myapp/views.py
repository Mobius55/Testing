from django.shortcuts import render
from .models import Item

# Create your views here.

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'myapp/item_detail.html', {'item': item})

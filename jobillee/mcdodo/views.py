from .models import item
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def openpos (request) :
	return render (request, 'mcdodo/openpos.html')

def orders(request) :
	return render (request, 'mcdodo/order.html')

def items(request):
	all_items = item.objects.all()


	return render(request, 'mcdodo/items.html', {
		'items': 	all_items
		})

def add_item(request):
	return render(request, 'mcdodo/add-item.html')
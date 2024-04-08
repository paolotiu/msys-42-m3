from .models import item, order, item_order
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


ERROR_CODES_TO_MESSAGES = {
	"NO_STOCK": "Not enough stock available"
}

SUCCESS_CODES_TO_MESSAGES = {
	"ORDER_SUCCESS": "Order has been placed successfully"
}

# Create your views here.
def openpos (request) :
	return render (request, 'mcdodo/openpos.html')

def orders(request) :
	items = item.objects.all()

	if 'error' in request.GET:
		error_code = request.GET.get('error')
		error_message = ERROR_CODES_TO_MESSAGES.get(error_code, "Unknown error")
		return render (request, 'mcdodo/order.html', {
			'items': items,
			'error': error_message
		})
	

	return render (request, 'mcdodo/order.html', {
		'items': items
	})

def items(request):
	all_items = item.objects.all()

	return render(request, 'mcdodo/items.html', {
		'items': 	all_items
		})


def confirm_order (request) :
	if (request.method == "POST"):
		p_method = request.POST.get('payment_method')
		items = request.POST.get('complete_order')
		total = request.POST.get('total_amount')

		ord = order.objects.create (total_amount=total, payment_type=p_method)

		item_fixed = items[:-1]
		stuff = item_fixed.split('-')
		for it in stuff:
			values = it.split(':')
			item_obj = item.objects.get(pk=values[0])
			it_price = item_obj.item_price
			lt = int(values[1]) * int(it_price)
			item_order.objects.create(item_id=item_obj, order_id=ord, line_total=lt, quantity=values[1])

			if item_obj.item_stock < int(values[1]):
				return redirect("/order?error=NO_STOCK")
				

			curr_item = item.objects.get(pk=values[0])
			curr_item.item_stock -= int(values[1])

			curr_item.save()

		return redirect("/order?success=ORDER_SUCCESS")

	return redirect("/order")


def add_item(request):
	if request.method == 'POST':
		item_name = request.POST.get('item_name')
		item_price = request.POST.get('item_price')

		item.objects.create(
			item_name = item_name,
			item_price = item_price
		)


	return redirect("/items")

def delete_item(request, pk):
	item.objects.filter(pk=pk).delete()
	return redirect("/items")


def update_item(request, pk):

	if request.method == 'POST':
		item_name = request.POST.get('item_name')
		item_price = request.POST.get('item_price')
		item_stock = request.POST.get('item_stock')


		item.objects.filter(pk=pk).update(
			item_name = item_name,
			item_price = item_price,
			item_stock = item_stock
		)

	return redirect("/items")


def pos_test(request):
	items = item.objects.all()


	return render(request ,'stuff/pos.html', {
		'items': items
	})

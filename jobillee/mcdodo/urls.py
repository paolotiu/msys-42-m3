from django.urls import path
from . import views

urlpatterns = [
	path('', views.orders, name = "order"),
	# items
	path('items/', views.items, name = "items"),
	path('order/', views.orders, name = "order"),
	path('add-item/', views.add_item, name = "add-item"),
	path('delete-item/<int:pk>/', views.delete_item, name = "delete-item"),
	path('update-item/<int:pk>/', views.update_item, name = "update-item"),
	path('pos-test/', views.pos_test, name = "pos-test"),
	path('confirm-order/', views.confirm_order, name = "confirm-order")
]
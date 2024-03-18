from django.urls import path
from . import views

urlpatterns = [
	path('', views.openpos, name = "openpos"),
	# items
	path('items/', views.items, name = "items"),
	path('order/', views.orders, name = "order"),
]
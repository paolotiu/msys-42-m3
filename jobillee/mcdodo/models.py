from django.db import models
from datetime import date
# Create your models here.
class item(models.Model): 

	item_name = models.CharField(max_length=100)
	item_price = models.DecimalField(max_digits=6, decimal_places=2)
	item_stock = models.IntegerField(default=0)
	objects = models.Manager()


	def getPrice(self):
		return self.item_price
	
	def getName(self):
		return self.item_name
	

	def __str__(self):
		return str(self.pk) + ":" + self.item_name


class order(models.Model):
	# Database fields should include: total amount paid, order date, payment type

	total_amount = models.DecimalField(max_digits=6, decimal_places=2)
	order_date = models.DateField(default=date.today)
	payment_type = models.CharField(max_length=100)
	objects = models.Manager()


	def __str__(self):
		return str(self.pk) + ":" + self.payment_type


class item_order(models.Model):
	# Database fields should include item_id, order_id, line_total, quantity 

	item_id = models.ForeignKey(item, on_delete=models.CASCADE)
	order_id = models.ForeignKey(order, on_delete=models.CASCADE)

	line_total = models.DecimalField(max_digits=9, decimal_places=2)
	quantity = models.IntegerField()

	objects = models.Manager()
	

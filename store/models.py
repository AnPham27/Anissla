from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name
	

class Top(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(max_length=200, null=True)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)
	in_stock= models.BooleanField(default=True)
	is_active= models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'Tops'

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Bottom(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(max_length=200, null=True)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)
	in_stock= models.BooleanField(default=True)
	is_active= models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'Bottoms'

	def __str__(self):
		return self.name
	
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	

class Shoe(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(max_length=200, null=True)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)
	in_stock= models.BooleanField(default=True)
	is_active= models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'Shoes'

	def __str__(self):
		return self.name
	
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	


class Accessory(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(max_length=200, null=True)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)
	in_stock= models.BooleanField(default=True)
	is_active= models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'Accessories'

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)
    
	def __str__(self):
		return str(self.id)


class OrderItem(models.Model):
	#for now, use top
	product = models.ForeignKey(Top, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	prov = models.CharField(max_length=200, null=False)
	postalcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
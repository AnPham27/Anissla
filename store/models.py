from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=200, null=True)
	slug = models.SlugField(max_length=50)
	category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)
	in_stock= models.BooleanField(default=True)
	is_active= models.BooleanField(default=True)

	def __str__(self):
		return self.name
	
	@staticmethod
	def get_all_products():
		return Product.objects.all()

	@staticmethod
	def get_all_products_by_id(category_id):
		if category_id:
			return Product.objects.filter(category = category_id)
		else:
			return Product.get_all_products();

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)
    
	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
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
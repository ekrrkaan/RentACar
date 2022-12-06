from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=20, null=True)
	email = models.CharField(max_length=200, null=True)
	Nationalid = models.CharField(max_length=30, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name
	
class Product(models.Model):
	CATEGORY = (
			 ('Sedan','Sedan'),
			 ('Coupe','Coupe'),
			 ('Sports Car','Sports Car'),
			 ('Station Wagon','Station Wagon'),
			 ('HatchBack','HatchBack'),
			 ('Convertible','Convertible'),
			 ('SUV','SUV'),
			 ('Minivan','Minivan'),
			 ('Pickup Truck','Pickup Truck'),
		 	 )
	name = models.CharField(max_length=200, null=True)
	manufacturer = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category =  models.CharField(max_length=200, null=True, choices=CATEGORY)
	description =  models.CharField(max_length=200, null=True, blank=True)
	color =  models.CharField(max_length=200, null=True)
	licenceplate = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name



class Rent(models.Model):
	Rented='Rented'
	Avaiable='Avaiable'
	STATUS = (
			 (Rented,'Rented'),
			 (Avaiable,'Avaiable'),
		 	 )


	customer =	models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200,choices=STATUS,default=Avaiable)

	def __str__(self):
		return self.product.name
	
	#BooleanField()

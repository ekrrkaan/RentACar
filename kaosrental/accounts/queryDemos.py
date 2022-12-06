import rent as Rent

from accounts import models
from accounts.models import customer, product

customers = customer.objects.all()

firstCustomer = customer.objects.first()

lastCustomer = customer.objects.last()

customerByName = customer.objects.get(name='Johnny Rasim')

customerById = customer.objects.get(id=14151617181)

firstCustomer.rent_set.all()

rent = Rent.objects.first()
parentName = rent.customer.name
products = product.objects.filter(category="available","rented")

leastToGreatest = product.objects.all().order_by('licenceplate')
greatestToLeast = product.objects.all().order_by('-licenceplate')
productsFiltered = product.objects.filter(tagsname="MINI","Audi","Land Rover","Mazda","Mercedes","Opel","Nissan","Seat","Skoda","Volvo","Volkswagen","KIA","Jeep","Hyundai","Peugeot","Honda","Renault","Fiat","Ford","BMW")

CarOrders = firstCustomer.rent_set.filter(productname="Car").count()

allRents = {}

for rent in firstCustomer.rent_set.all():
    if rent.product.name in allRents:
        allRents[rent.product.name] += 1
    else:
        allRents[rent.product.name] = 1
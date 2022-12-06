from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import RentForm

# Create your views here.

def home(request):
    rent = Rent.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_rents = rent.count()
    Avaiable = rent.filter(status='Avaiable').count()
    Rented = rent.filter(status='Rented').count()


    context = {'rent':rent, 'customers':customers,
    'total_rents':total_rents,'Avaiable':Avaiable,
    'Rented':Rented }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk_test): 
    customer = Customer.objects.get(id=pk_test)

    Rent = customer.rent_set.all()
    rent_count = Rent.count()

    context = {'customer':customer, 'Rent':Rent, 'rent_count':rent_count}
    return render(request, 'accounts/customer.html',context)

def createRent(request, pk):
    customer = Customer.objects.get(id=pk)
    form = RentForm(initial={'customer':customer})
    if request.method == 'POST':
        print('printing POST:', request.POST)
        form = RentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')



    context = {'form':form}
    return render(request, 'accounts/rent_form.html', context)

def updateRent(request, pk):

    rent = Rent.objects.get(id=pk)
    form = RentForm(instance=rent)

    if request.method == 'POST':
        print('printing POST:', request.POST)
        form = RentForm(request.POST, instance=rent)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/rent_form.html', context)

def deleteRent(request, pk):
    rent = Rent.objects.get(id=pk)
    if request.method == "POST":
        rent.delete()
        return redirect('/')

    context = {'item':rent}
    return render(request, 'accounts/delete.html', context)



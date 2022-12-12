from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import RentForm , CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)




def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
def customer(request, pk_test): 
    customer = Customer.objects.get(id=pk_test)

    Rent = customer.rent_set.all()
    rent_count = Rent.count()

    context = {'customer':customer, 'Rent':Rent, 'rent_count':rent_count}
    return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteRent(request, pk):
    rent = Rent.objects.get(id=pk)
    if request.method == "POST":
        rent.delete()
        return redirect('/')

    context = {'item':rent}
    return render(request, 'accounts/delete.html', context)


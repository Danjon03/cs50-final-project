
from django.contrib import admin
from .models import currentlyLoggedInUsers, Users, Inventory, Employee, Order
# Register your models here.
admin.site.register(currentlyLoggedInUsers)
admin.site.register(Users)
admin.site.register(Inventory)
admin.site.register(Employee)
admin.site.register(Order)

from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'

from django import forms

class OrderForm(forms.Form):
	size = forms.CharField(label='size', max_length=10)
	quantity = forms.IntegerField(label="quantity")
	ingredient1 = forms.CharField(label="ingredient1")
	ingredient2 = forms.CharField(label="ingredient2")
	ingredient3 = forms.CharField(label="ingredient3")




class LoginForm(forms.Form):
	name = forms.CharField(label='name', max_length=64)
	username = forms.CharField(label='username', max_length=64)
	password = forms.CharField(label='password', max_length=164)
from django.db import models

# Create your models here.


class currentlyLoggedInUsers(models.Model):
	username = models.CharField(max_length=64)
	
	
	def __str__(self):
		return f"{self.username} is logged in with order number {self.order}"
		
		
class Users(models.Model):
	first_name = models.CharField(max_length = 64, null = True)
	username = models.CharField(db_column="username_id", primary_key=True, max_length=64, null=False)
	password = models.CharField(max_length=64, null=True)
	staffStatus = models.NullBooleanField(null=True)
	
	def __str__(self):
		return f"{self.first_name} is user {self.username}"
		

class Inventory(models.Model):
	itemName = models.CharField(max_length = 64, null = True)
	quantity = models.IntegerField(null=True)
	productCode = models.IntegerField(null=True)
	productPrice = models.IntegerField(null=True)
	suggustedQuantity = models.IntegerField(null=True)
	
	def __str__(self):
		return f"{self.itemName}"

class Employee(models.Model):
	name = models.CharField(max_length = 64, null = True)
	
	def __str__(self):
		return f"{self.name}"


class Order(models.Model):
	code = models.IntegerField(null = True)
	itemsNeededCodes = models.TextField(null = True)
	itemsNeededQuantities = models.TextField(null = True)
	
	def __str__(self):
		return f"{self.code} contains {self.itemsNeededCodes}"
	
from django.test import TestCase

# Create your tests here.

from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
	path("", views.login, name="login"),
	path("admin/", admin.site.urls),
	path("createAccount", views.createAccount, name="createAccount"),
	path("inBetweenCreateAccount", views.inBetweenCreateAccount, name="inBetweenCreateAccount"),
	path("inBetweenLogin", views.inBetweenLogin, name="inBetweenLogin"),
	path("logout", views.logout, name="logout"),
	path("inventory", views.inventory, name="inventory"),
	path("home", views.home, name="home"),
	path("employee", views.employee, name="employee"),
	path("shortages", views.shortages, name="shortages"),
	path("addEmployees", views.addEmployees, name="addEmployees"),
	path("createEmployee", views.createEmployee, name="createEmployee"),
	path("removeEmployee", views.removeEmployee, name="removeEmployee"),
	path("<x>/deleteEmployee", views.deleteEmployee, name="deleteEmployee"),
	path("allOrders", views.allOrders, name="allOrders")

]


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import currentlyLoggedInUsers, Users, Inventory, Employee
from .forms import OrderForm, LoginForm
from django.urls import reverse
from django.template import RequestContext
import datetime
# Create your views here.


def login(request):
	
	
		return render(request, "login.html")
	
def createAccount(request):
	
	
	# Takes you to the checkout screen if you have already created an order
	
	if 'code' in request.COOKIES:
		x = request.COOKIES['code']
		#print("--------------------", x, "--------------------------------")
		size = Order.objects.filter(code=x).values_list('size')[0][0]
		quantity = Order.objects.filter(code=x).values_list('quantity')[0][0]
		price = Order.objects.filter(code=x).values_list('price')[0][0]
		ingredient1 = Order.objects.filter(code=x).values_list('topping1')[0][0]
		ingredient2 = Order.objects.filter(code=x).values_list('topping2')[0][0]
		ingredient3 = Order.objects.filter(code=x).values_list('topping3')[0][0]
	
		#print("--------------------", size, quantity, price, ingredient1, ingredient2, ingredient3, "-------------------")
		context = {"code": x, "size": size, "quantity": quantity, "price": price,
		"ingredient1": ingredient1, "ingredient2": ingredient2, "ingredient3": ingredient3}
		
				
		return render(request, "checkout.html", context)
	
	# Takes the user to prices if they are already logged in but have not created an order yet
	
	elif 'username' in request.COOKIES and 'userInfo' in request.COOKIES:
		username = request.COOKIES['username']
		print("----------------", username, "--------------------")
		userInfo = request.COOKIES['userInfo']
		print("----------------", userInfo, "--------------------")
		context={
			"PizzaPrices": PizzaPrices.objects.all(),
			"userInfo": request.COOKIES['userInfo'],
			"username": request.COOKIES['username']
			}
		return render(request, "prices.html", context)
	
	
		
	
	
	
	else:
		return render(request, "createAccount.html")

def inBetweenCreateAccount(request):
	

	loginForm = LoginForm(request.POST)
	if loginForm.is_valid():
		
		try:
			newUser = Users.objects.create(first_name=loginForm.cleaned_data["name"], username=loginForm.cleaned_data["username"], password=loginForm.cleaned_data["password"])
			newUser.save()
			print(newUser)
			User= currentlyLoggedInUsers(username=newUser.first_name)
			User.save()
			context = {"userInfo": newUser.first_name,
			"Ingredients": Ingredients.objects.all()}
			return render(request, "prices.html", context)
			
			
		except:	
			context={"message": "Your username, password, or name have already been taken. Try again."}
			return render(request, "createAccount.html", context)
	
def inBetweenLogin(request):
	loginForm = LoginForm(request.POST)
	if loginForm.is_valid():
	
	 
		
		#try:
		Username = Users.objects.filter(username=loginForm.cleaned_data["username"]).values_list('username')[0][0]
		#print("------------------",str(a), " ------------------")
			
		Password = Users.objects.filter(password=loginForm.cleaned_data["password"]).values_list('password')[0][0]
		
		Name = Users.objects.filter(username=loginForm.cleaned_data["username"]).values_list('first_name')[0][0]
		#print("-------------------", str(Name), "---------------------")
			
		
		
		context = {
			
			"userInfo": str(Name), 
			"username": str(Username)
			
		
		}
		
		
		
		staff = Users.objects.filter(username=loginForm.cleaned_data["username"]).values_list('staffStatus')[0][0]
		
		if bool(staff) == False:
			response = render(request, "employeeHome.html")
			response.set_cookie('username', Username)
			
		else:
			response = render(request, "home.html")
			response.set_cookie('username', Username)
		return response
		
		
		
		
		
		
	else:
		return render(request, "login.html")
	
def logout(request):
	
	response = render(request, 'login.html')
	response.delete_cookie('username')
	return response

def inventory(request):
	context = {"inventory": Inventory.objects.all()}
	return render(request, "inventoryDatabase.html", context)
	
def home(request):
	response = render(request, "home.html")
	
	x = request.COOKIES["username"]
	
	staff = Users.objects.filter(username=x).values_list('staffStatus')[0][0]
		
	if bool(staff) == True:
		response = render(request, "home.html")
	else:
		response = render(request, "employeeHome.html")

	return response
	
def employee(request):
	context = {"employees": Users.objects.all()}
	return render(request, "employees.html", context)

def shortages(request):
	context ={"inventory": Inventory.objects.all()}
	return render(request, "shortages.html", context)

def addEmployees(request):
	return render(request, "addEmployees.html")
	
def createEmployee(request):
	loginForm = LoginForm(request.POST)
	if loginForm.is_valid():
		
		newEmployee = Employee(name=loginForm.cleaned_data["name"])
		newEmployee.save()
		newUser = Users(first_name=loginForm.cleaned_data["name"], username=loginForm.cleaned_data["username"], password=loginForm.cleaned_data["password"], staffStatus=False)
		newUser.save()
		return render(request, "home.html")



def removeEmployee(request):
	context = {"employees": Users.objects.all()}
	return render(request, "removeEmployee.html", context)
	

def deleteEmployee(request, x):
	Users.objects.filter(first_name=x).delete()
	
	context = {"employees": Users.objects.filter(staffStatus__gt=True)}
	return render(request, "removeEmployee.html", context)


def allOrders(request):
	context ={"inventory": Inventory.objects.all()}
	
	return render(request, "allOrders.html", context)






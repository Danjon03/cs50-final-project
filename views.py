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
	context = {"employees": Employee.objects.all()}
	return render(request, "employees.html", context)
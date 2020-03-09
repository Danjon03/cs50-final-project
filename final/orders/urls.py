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


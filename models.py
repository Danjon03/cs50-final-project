from django.db import models

# Create your models here.


class currentlyLoggedInUsers(models.Model):
	username = models.CharField(max_length=64)
	order = models.IntegerField(null=True)
	
	def __str__(self):
		return f"{self.username} is logged in with order number {self.order}"
		
		
class Users(models.Model):
	first_name = models.CharField(max_length = 64, null = True)
	username = models.CharField(db_column="username_id", primary_key=True, max_length=64, null=False)
	password = models.CharField(max_length=64, null=True)
	
	def __str__(self):
		return f"{self.first_name} is user {self.username}"
		

class Inventory(models.Model):
	itemName = models.CharField(max_length = 64, null = True)
	quantity = models.IntegerField(null=True)
	productCode = models.IntegerField(null=True)
	productPrice = models.IntegerField(null=True)
	
	def __str__(self):
		return f"{self.itemName}"
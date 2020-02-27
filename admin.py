from django.contrib import admin
from .models import currentlyLoggedInUsers, Users, Inventory
# Register your models here.
admin.site.register(currentlyLoggedInUsers)
admin.site.register(Users)
admin.site.register(Inventory)

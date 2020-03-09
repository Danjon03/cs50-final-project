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
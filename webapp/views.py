from django.shortcuts import render
from django.contrib.auth import *
from users.models import customeUser
from webapp.forms import *
from users import *

# Create your views here.
def showDataEntryForm(req):
	return render(req,'dataEntryForm.html')

def signupform(req):
	return render(req,'signupform.html')

def register(req):

	if req.method == 'POST':
		email = req.POST['email']
		password = req.POST['password']
		form = customeUser(email=email,password=password)
		form.save()
		return render(req,'login.html')


	form = customeUser()

	print(form)
	return render(req,'signupform.html',{"form":form})
def login(req):
	if req.method == 'POST':
		email = req.POST['email']
		password = req.POST['password']
		user = authenticate(req,email=email,password=password)
		if user is None:
			return render(req,'login.html')
		else:
			return  render(req,'home.html')
	else:
		return  render(req,'login.html')
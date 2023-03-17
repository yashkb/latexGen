from django.shortcuts import render
from django.contrib.auth import *
from users.models import customeUser
from webapp.forms import *
from users import *
from django.http import *

# Create your views here.
def showDataEntryForm(req):
	return render(req,'dataEntryForm.html')

def signupform(req):
	return render(req,'signupform.html')

def register(req):

	if req.method == 'POST' and req.POST:
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
		user = authenticate(req,username=email,password=password)
		if user is None:
			return render(req,'login.html')
		else:
			return  render(req,'home.html')
	else:
		return  render(req,'login.html')

def dregister(req):
	return render(req,'users/signup.html')

def latexSample(req):
	title = req.POST['title']
	noOfSection = req.POST['noOfSection']

	noOfSection = int(noOfSection)
	list = []
	list.append(title)
	for i in range(noOfSection):
		i = str(i)
		titletxt = req.POST['titletxt'+i]
		txtarea = req.POST['txtarea'+i]
		list.append(titletxt)
		list.append(txtarea)

	return render(req,'latexSample.html',{'data':list})
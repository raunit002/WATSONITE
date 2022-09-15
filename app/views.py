from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import Contact
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm

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
			

		context = {'form':form}
		return render(request,'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request,'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



# Create your views here.
def Index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')   

def contact(request):
    #return HttpResponse("this is contact page")   
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact.objects.create(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!!')
        # return render(request, 'contact.html', {'form': contact(request.GET)})
        
    
    return render(request,'contact.html')    


def services(request):
    return render(request,'services.html') 

def works(request):
    return render(request,'works.html') 

def testimonial(request):
    return render(request,'testimonial.html')

def crypto(request):
    return render(request,'crypto.html')


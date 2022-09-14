from pyexpat import model
from django.shortcuts import render,redirect
from app.models import Contact
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
 


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


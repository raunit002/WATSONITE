from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')   

def contact(request):
    return render(request,'contact.html') 

def services(request):
    return render(request,'services.html') 

def works(request):
    return render(request,'works.html') 

def testimonial(request):
    return render(request,'testimonial.html')

def crypto(request):
    return render(request,'crypto.html')

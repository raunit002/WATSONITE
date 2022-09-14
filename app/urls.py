from django.contrib import admin
from django.urls import path
from app import views
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path("", views.Index, name='home'),
    path('about', views.about,name='about'),
    path('contacts', views.contact,name='contact'),
    path('services', views.services,name='services'),
    path('works', views.works,name='works'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('crypto', views.crypto,name='crypto'),
   

]

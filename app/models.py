from django.db import models
from django.forms import forms


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


# class UserForm(forms.ModelForm):
#     class Meta:
#           model = User
#           fields = ["username", "email", "password"]


  #To diaplay name in the database
    def __str__(self):
          return self.name
from django.contrib import admin
from app.models import Contact
from app.views import contact
# Register your models here.
admin.site.register(Contact)
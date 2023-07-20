from django.contrib import admin

# Register your models here.
from .models import Page, UserData

admin.site.register(Page)
admin.site.register(UserData)
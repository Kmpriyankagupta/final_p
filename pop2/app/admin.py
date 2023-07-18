from django.contrib import admin

# Register your models here.
from .models import Page, MyModel

admin.site.register(Page)
admin.site.register(MyModel)
from django.db import models

# Create your models here.
class Page(models.Model):
    pagename = models.CharField(max_length=100)
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=600)
    keywords = models.CharField(max_length = 600, null=True, blank=True)

    def __str__(self):
        return self.pagename
    
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobilenumber = models.IntegerField()
    typeservicerequired =models.CharField(max_length=20)

    def __str__(self):
        return self.name
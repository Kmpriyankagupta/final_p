from django.db import models

# Create your models here.
class Page(models.Model):
    pagename = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    keywords = models.CharField(max_length = 10000, null=True, blank=True)

    def __str__(self):
        return self.pagename
    
class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobilenumber = models.IntegerField()
    typeservicerequired =models.CharField(max_length=20)

    def __str__(self):
        return self.name
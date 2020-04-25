from django.db import models

# Create your models here.
class Home(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(null=True,blank=True)
    slug=models.SlugField(max_length=200)
    description=models.TextField(max_length=200)
    price=models.CharField(max_length=200)
    rent=models.BooleanField(default=True,blank=True)
    sale=models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.name

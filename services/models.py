from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#complete Pricing-model
class Pricing(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.title


#complete Services-model
class Services(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Ability ( models.Model):
    ability = models.CharField( max_length=200)
    def __str__(self):
        return self.ability
#complete Agents-model

class Agents(models.Model):
    name = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to="agent", default="default.jpg")
    ability = models.ForeignKey( Ability , on_delete=models.CASCADE)

    def __str__(self):
        return self.name














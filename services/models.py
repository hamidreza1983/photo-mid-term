from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Pricing - model
class Pricing(models.Model):
    service = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.service


# Services - model
class Services(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Abiliti - model
class Ability ( models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


# Agents - model
class Agent(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ability = models.ManyToManyField(Ability)
    image = models.ImageField(upload_to="agent", default="default.jpg")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user
    
    
# Testimonials - model
class Testimonials(models.Model):
    stars = models.IntegerField()
    text = models.CharField( max_length=200)
    image = models.ImageField(upload_to="testimonial", default="default.jpg")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)











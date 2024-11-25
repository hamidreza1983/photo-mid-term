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


# Ability - model
class Ability (models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


# Agents - model
class Agent(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="agent", default="default.jpg")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user
    
    
# Testimonials - model
class Score(models.Model):
    count = models.IntegerField(default=5)

    def __str__(self):
        return str(self.count)

class Testimonials(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="tester", default="default.jpg")
    content = models.TextField()
    domain = models.CharField(max_length=30)
    stars = models.ForeignKey(Score, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def stars_count(self):
        return range(self.stars.count)










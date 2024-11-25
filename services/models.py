from django.db import models

# Create your models here.


#complete Pricing-model
class Pricing(models.Model):
    pass


#complete Services-model
class Services(models.Model):
    pass


#complete Agents-model
class Agents(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="agents", default="default.jpg")
    ability = models.CharField(max_length=100)

    def __str__(self):
        return self.name

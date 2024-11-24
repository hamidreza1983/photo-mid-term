from django.db import models
from services.models import Agents


#complete category-model
class Category(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

#complete gallery-model
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallary",default="default.jpg")
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    title = models.CharField( max_length=200)
    desc = models.TextField()
    image_agent = models.ForeignKey(Agents, on_delete=models.CASCADE)
    cat = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    project_date = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

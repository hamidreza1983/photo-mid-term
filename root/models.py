from django.db import models
from services.models import Agent


# Category - model
class Category(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

# Project_info - model
class Project_info(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    client = models.CharField(max_length=20)
    project_date = models.DateTimeField(auto_now_add=True)
    project_url = models.CharField(max_length=200)
    status = models.BooleanField(default=False)


# Gallery_single - model
class Gallery_single(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    agent_description = models.TextField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    description = models.TextField()
    project_info = models.ForeignKey(Project_info, on_delete=models.CASCADE)


# Gallery - model
class Gallery(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="picture")
    zoom = models.ImageField(upload_to="zoon")
    galler_single = models.ForeignKey(Gallery_single, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


    

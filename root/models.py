from django.db import models
from services.models import Agent


# Category - model
class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

# Gallery - model
class Gallery(models.Model):
    #gallery-single :
    picture = models.ImageField(upload_to="picture",default="default.jpg" )
    title = models.CharField(max_length=200)
    content = models.TextField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    agent_description = models.TextField()
    description = models.TextField()
        #project-info :
    category = models.ManyToManyField(Category)
    client = models.CharField(max_length=200)
    project_date = models.DateTimeField(auto_now_add=True)
    project_url = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title



from django.db import models
from services.models import Agents



#complete category-model
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


#complete gallery-model
class Gallery(models.Model):
    image1 = models.ImageField(upload_to="gallery", default="default.jpg")
    image2 = models.ImageField(upload_to="gallery", default="default.jpg")
    image3 = models.ImageField(upload_to="gallery", default="default.jpg")
    image4 = models.ImageField(upload_to="gallery", default="default.jpg")
    image5 = models.ImageField(upload_to="gallery", default="default.jpg")
    image6 = models.ImageField(upload_to="gallery", default="default.jpg")
    image7 = models.ImageField(upload_to="gallery", default="default.jpg")
    title = models.CharField(max_length=100)
    content = models.TextField()
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE)
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    client = models.CharField(max_length=100)
    project_date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.url







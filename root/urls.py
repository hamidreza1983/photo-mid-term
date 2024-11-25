from django.urls import path
from .views import *

app_name = "root"

# create your root`s urls
urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("gallery",gallery , name="gallery"),
    path("detail/<int:id>", gallery_detail, name="gallery-details"),
]
    




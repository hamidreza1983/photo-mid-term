from django.urls import path
from .views import *


# create your root`s urls
urlpatterns = [
    path("/", home, name="home"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("detail/<int:id>", gallery_details, name="gallery-details"),
]

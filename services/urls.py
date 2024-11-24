from django.urls import path
from .views import *


# create your root`s urls
urlpatterns = [
    path("/", services, name="services"),
]

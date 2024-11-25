from django.urls import path
from .views import *


app_name = "services"

# create your root`s urls
urlpatterns = [
    path("services",services , name="services"),
]    

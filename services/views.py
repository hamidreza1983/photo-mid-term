from django.shortcuts import render , get_object_or_404
from .models import Services



#complete services view
def services(request):
    return render(request,'services/services.html')
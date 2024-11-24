from django.shortcuts import render



#complete services view
def services(request):
    return render(request,'services/services.html')

from django.shortcuts import render , get_object_or_404
from .models import Services


def services(request):
    service = Services.objects.filter(status=True)
    price = Pricing.objects.filter(status=True)
    tester = Testimonials.objects.filter(status=True)
    context = {
        "services": service,
        "price" : price,
        "tester" : tester,
    }
    return render(request,'root/services.html',context=context)






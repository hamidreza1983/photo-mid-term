from django.shortcuts import render , get_object_or_404
from .models import Gallery
from services.models import Testimonials

#complete home view
def home(request):
    gallery = Gallery.objects.filter(status=True)[:8]
    context = {
        'gallery' : gallery,
    }
    return render(request,'root/index.html',context=context)


#complete about view
def about(request):
    testers = Testimonials.objects.filter(status=True)
    context = {
        'testers' : testers,
    }
    return render(request,'root/about.html',context=context)


#complete contact view
def contact(request):
    return render(request,'root/contact.html')

#
def gallery(request):
    gallery = Gallery.objects.filter(status=True)
    context = {
        'gallery' : gallery,
    }
    return render(request,'root/gallery.html' , context=context )

def gallery_detail(request,id):
    gallery = get_object_or_404(Gallery,id=id)
    context = {
        'gallery' : gallery
    }
    return render(request,'root/gallery-single.html',context=context)





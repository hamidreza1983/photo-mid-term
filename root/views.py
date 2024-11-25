from django.shortcuts import render, get_object_or_404
from .models import Gallery



#complete home view
def home(request):
    pictures = Gallery.objects.all()
    context = {
        'gallery' : pictures
    }
    return render (request, 'root/index.html', context=context)


#complete about view
def about(request):
    pass


#complete contact view
def contact(request):
    pass


# create and comlete gallery detail view
def gallery_details(request, id):
    item = get_object_or_404(Gallery, id=id)
    context = {
        'item' : item
    }
    return render (request, 'root/gallery-single.html', context=context)
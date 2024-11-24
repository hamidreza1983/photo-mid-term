from django.shortcuts import render



#complete home view
def home(request):
    return render(request,'root/index.html')


#complete about view
def about(request):
    return render(request,'root/about.html')




#complete contact view
def contact(request):
    return render(request,'root/contact.html')




# create and comlete gallery detail view
def gallery_details(request):
    return render(request,'root/gallery-single.html')


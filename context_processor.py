from root.models import Category




def context_object(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return context
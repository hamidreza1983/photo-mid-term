from root.models import Category

def general_context(request):
    context = {
        'categories' : Category.objects.filter(status=True)
    }

    return context
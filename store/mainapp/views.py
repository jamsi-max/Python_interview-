from django.shortcuts import render
from mainapp.models import Product

def index(request):
    content = {
        'title': 'Main',
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/main_base.html', context=content)

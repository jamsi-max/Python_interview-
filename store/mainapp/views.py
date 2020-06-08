from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse
from django.forms.models import model_to_dict

from mainapp.models import Product
from mainapp.forms import CreateProductForm


class ProductList(View):
    def get(self, request):
        content ={
            'form': CreateProductForm(),
            'products': Product.objects.all(),
        }
        return render(request, 'mainapp/main_base.html', context=content)

    def post(self, request):
        form = CreateProductForm(request.POST)
        
        if form.is_valid():
            new_product = form.save()
            # return redirect('main:index')
            return JsonResponse({'product': model_to_dict(new_product)})
        else:
            return redirect('main:index')
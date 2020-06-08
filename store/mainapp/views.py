from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.template.loader import render_to_string

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
        form = CreateProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()

            result = render_to_string('mainapp/includes/inc__product_list.html', context={'products': Product.objects.all()})
            return JsonResponse({'result': result})
        else:
            return redirect('main:index')
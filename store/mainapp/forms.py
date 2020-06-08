from django import forms

from .models import Product

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name","desc", "price", "image", "quantity")

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'})
        }


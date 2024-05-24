from django.forms import ModelForm
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'featured_image', 'description', 'weight', 'size', 'categories', 'demo_link']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Title'}
        )

        self.fields['featured_image'].widget.attrs.update(
            {'class': 'form-control', 'id':'formFile'}
        )

        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Description'}
        )

        self.fields['weight'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'weight'}
        )

        self.fields['size'].widget.attrs.update({
            'class': 'choices form-select',
            'multiple': 'multiple'
        })

        self.fields['categories'].widget.attrs.update({
            'class': 'choices form-select',
            'multiple': 'multiple'
        })
        
        self.fields['demo_link'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'demo_link'}
        )
        

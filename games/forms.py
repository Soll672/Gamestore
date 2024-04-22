from django import forms
from .models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'category', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text']

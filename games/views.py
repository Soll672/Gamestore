from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Review, Tag
from .forms import ProductForm
from .forms import ReviewForm
import random
import datetime

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'games/create_product.html', {'form': form})

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'games/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', id=id)
    else:
        review_form = ReviewForm()
    reviews = product.reviews.all()
    return render(request, 'games/product_detail.html', {'product': product, 'reviews': reviews, 'review_form': review_form})

def hello_view(request):
    return HttpResponse("Hello! It's my project")

def fun_view(request):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet."
    ]
    return HttpResponse(random.choice(jokes))

def main_view(request):
    current_time = datetime.datetime.now()
    return HttpResponse(f"<html><body><h1>Welcome to GameStore!</h1><p>Current date and time: {current_time}</p></body></html>")

def home_view(request):
    return HttpResponse("<html><body><h1>Welcome to the GameStore!</h1></body></html>")





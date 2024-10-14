# app4/views.py
from django.shortcuts import render
from .models import Products
from django.db.models import Q
import numpy as np
import pandas as pd
from django.shortcuts import render
from .models import Products

def product_list(request):
    products = Products.objects.all()

    selected_size = request.GET.get('size', None)
    
    if selected_size:
        products = products.filter(size=selected_size)

    df = pd.DataFrame(list(products.values()))

    price_ranges = [(0, 50), (51, 100), (101, 150), (151, 250), (251, 500)]

    return render(request, 'app4/product_list.html', {
        'products': df.to_dict(orient='records'),  
        'price_ranges': price_ranges,
        'num_segments': 8,  
        'sizes': ['Small', 'Medium', 'Large']  
    })


def home(request):
    return render(request, 'app4/home.html')


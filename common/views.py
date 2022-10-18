from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    context = {
        'categories': Category.objects.all()[:6],
        'latest_products': Product.objects.all()[:6]
    }
    return render(request, "../templates/admin/index.html", context)

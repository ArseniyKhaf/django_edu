from django.http import HttpResponse
from django.shortcuts import render

from main.models import Category, Goods


def index(request):
    goods = Goods.objects.all()
    context = {
        "products": goods,
    }
    return render(request,
                  template_name="main/index.html",
                  context=context,
                  )


def main(request):
    return render(request, template_name="main/index.html")


def profil(request):
    return render(request, template_name="main/index.html")


def drink(request):
    category = Category.objects.get(name="Напитки")
    goods = Goods.objects.filter(category=category)
    context = {
        "products": goods,
    }
    return render(request,
                  template_name="main/drink.html",
                  context=context,
                  )

from django.http import HttpResponse
from django.shortcuts import render

from main.models import Category, Goods


def index(request):
    goods = Goods.objects.all()
    context = {
        "products": goods,
        "categories": Category.objects.all(),
    }
    return render(request,
                  template_name="main/index.html",
                  context=context,
                  )


def profil(request):
    return render(request, template_name="main/index.html")


def category_view(request, slug):
    goods = Goods.objects.filter(category__slug=slug)
    context = {
        "products": goods,
        "categories": Category.objects.all(),
    }
    return render(request,
                  template_name="main/index.html",
                  context=context,
                  )


def detail_view(request, slug):
    context = {
        "product": Goods.objects.get(slug=slug),
    }
    return render(request,
                  template_name="main/detail.html",
                  context=context,
                  )

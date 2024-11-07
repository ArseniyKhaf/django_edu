from django.http import HttpResponse
from django.shortcuts import render

from main.models import Category, Feedback, Goods


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
    goods = Goods.objects.get(slug=slug)
    context = {
        "product": Goods.objects.get(slug=slug),
        "categories": Category.objects.filter(),
        "feedback": Feedback.objects.all(),

    }
    return render(request,
                  template_name="main/detail.html",
                  context=context,
                  )


def basket(request):
    context = {
        "product": Goods.objects.all(),
        "categories": Category.objects.filter(),
    }
    return render(request,
                  template_name="main/basket.html",
                  context=context,
                  )

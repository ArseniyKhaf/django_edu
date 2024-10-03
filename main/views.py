from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, template_name="main/index.html")


def profil(request):
    return render(request, template_name="main/index.html")

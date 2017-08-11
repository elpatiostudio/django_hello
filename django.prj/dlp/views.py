from django.shortcuts import render
from shows.models import Show
from main.models import Member
from data.news import NEWS
from products.models import Product, Category
from gallery.models import Gallery


def home(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'features': ['cheap', 'fast', 'easy', ],
    }
    return render(request, 'home.html', context)


def products(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'products_list': Product.objects.all(),
        'category_list': Category.objects.all(),
    }

    return render(request, 'products.html', context)


def members(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'members': Member.objects.all(),
    }
    return render(request, 'members.html', context)


def news(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'news': NEWS,
    }
    return render(request, 'news.html', context)


def gallery(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'gallery': Gallery.objects.all(),


    }
    return render(request, 'gallery.html', context)


def shows(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'shows': Show.objects.all(),
    }
    return render(request, 'shows.html', context)

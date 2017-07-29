from django.shortcuts import render
from data.members import MEMBERS
from data.shows import SHOWS_LIST
from main.models import Member
from data.news import NEWS


def home(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'features': ['cheap', 'fast', 'easy', ],
    }
    return render(request, 'home.html', context)


def contact(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
    }
    return render(request, 'contact.html', context)


def products(request):
    name = request.GET.get('name', 'User')
    product = request.GET.get('product', 'No Products Avaliable').split(',')
    context = {
        'name': name,
        'products_list': product,
    }

    return render(request, 'products.html', context)

def team(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
    }
    return render(request, 'team.html', context)

def members(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'members': Member.objects.all(),
    }
    return render(request, 'members.html', context)

def portfolio(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
    }
    return render(request, 'portfolio.html', context)

def services(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
    }
    return render(request, 'services.html', context)


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
    }
    return render(request, 'gallery.html', context)

def shows(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'shows': SHOWS_LIST,
    }
    return render(request, 'shows.html', context)

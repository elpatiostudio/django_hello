from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'features': ['cheap', 'fast', 'easy', ],
    }
    return render(request, 'base.html', context)


def contact(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
    }
    return render(request, 'contact.html', context)


urlpatterns = [
    url('^$', home),
    url('^contact/', contact),
]

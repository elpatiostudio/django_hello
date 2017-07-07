from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = request.GET['name']
    context = {
        'name': name
    }
    return render(request, 'base.html', context)


urlpatterns = [
    url('', home),
]

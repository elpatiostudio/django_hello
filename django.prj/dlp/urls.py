from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	name = request.GET['name']
	return render(request, 'base.html', {'name': name})


urlpatterns = [
    url('', index),
]

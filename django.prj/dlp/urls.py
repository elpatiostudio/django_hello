from django.conf.urls import url
from django.http import HttpResponse


def index(request):
	return HttpResponse('Hello World 2')

def bye(request):
	return HttpResponse('Chau')


urlpatterns = [
    url('hello/', index),
    url('bye/', bye),
]

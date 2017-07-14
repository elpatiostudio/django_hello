from django.conf.urls import url
from views import home, contact, products


urlpatterns = [
    url('^$', home),
    url('^contact/', contact),
    url('^products/', products),
    url('^services/', services),
]

from django.conf.urls import url

from views import home, contact, products, team, members, portfolio, services



urlpatterns = [
    url('^$', home),
    url('^contact/', contact), 
    url('^team/', team),
    url('^products', products),
    url('^members', members), 
    url('^portfolio/', portfolio),
    url('^services/', services),
    url('^shows/', shows),
]

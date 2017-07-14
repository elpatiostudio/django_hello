from django.conf.urls import url
from views import home, contact, products, team


urlpatterns = [
    url('^$', home),
    url('^contact/', contact), 
    url('^team/', team),
    url('^products', products), 
]

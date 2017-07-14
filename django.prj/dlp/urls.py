from django.conf.urls import url
from views import home, contact, team


urlpatterns = [
    url('^$', home),
    url('^contact/', contact), 
    url('^team/', team),
]

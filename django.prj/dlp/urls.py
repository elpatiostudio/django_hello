from django.conf.urls import url
from views import home, contact


urlpatterns = [
    url('^$', home),
    url('^contact/', contact),
]

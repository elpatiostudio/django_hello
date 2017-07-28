from django.conf import settings
from django.conf.urls import url
from django.contrib import admin

from views import home, contact, products, team, members, portfolio, services, news, shows



urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url('^$', home),
    url('^contact/', contact),
    url('^team/', team),
    url('^products', products),
    url('^members', members),
    url('^portfolio/', portfolio),
    url('^services/', services),
    url('^shows/', shows),
    url('^news/', news),
]

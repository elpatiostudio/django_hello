from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from views import home, products, members, news, shows, gallery


urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url('^$', home),
    url('^products', products),
    url('^members', members),
    url('^shows/', shows),
    url('^news/', news),
    url('^gallery/', gallery),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from alpha.views import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home, name="home"),
    url(r'^legal/', include("alpha.urls.policy", namespace="legal")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

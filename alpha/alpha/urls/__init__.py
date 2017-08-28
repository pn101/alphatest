from django.conf.urls import url, include
from django.contrib import admin

from alpha.views import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home, name="home"),
    url(r'^legal/', include("alpha.policy", namespace="legal")),
]

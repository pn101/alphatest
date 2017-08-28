from django.conf.urls import url, include

from alpha.views import *


urlpatterns = [
    url(r'^aboutus/$', aboutus, name="aboutus"),
    url(r'^termsandconditions/$', terms, name="terms"),
    url(r'^policy/$', policy, name="policy"),
]

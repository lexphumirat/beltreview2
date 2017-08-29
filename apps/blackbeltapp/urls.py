from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^logmein$', views.logmein),
    url(r'^friends/(?P<id>\d+)$' , views.logmein)


]

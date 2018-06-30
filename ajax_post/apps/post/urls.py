from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^postpage$', views.postpage),
    url(r'^makepost$', views.makepost)
]

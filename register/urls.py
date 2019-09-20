from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create', create_object, name='create'),
    url(r'^lists', list_object, name='list')   
]

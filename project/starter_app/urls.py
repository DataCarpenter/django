from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<slug_tag>.+)$', views.onepost,),
]

from django.conf.urls import url
from . import views  

urlpatterns = [
    url(r'^amadon$', views.index),
    url(r'^amadon/checkout$', views.checkout),
    url(r'^amadon/buy$', views.buy)
]
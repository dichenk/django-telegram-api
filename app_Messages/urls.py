from django.urls import path
from . import views

urlpatterns = [
    path('send', views.send_messages),
    path('get', views.get_messages),
]
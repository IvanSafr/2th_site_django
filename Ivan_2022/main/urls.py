from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main),
    path('info', views.info),
    path('connection', views.us)
]
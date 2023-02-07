from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main, name="home"),
    path('about-us', views.info, name="us"),
    path("new_note", views.create , name="create"),
]
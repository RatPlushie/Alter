from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('upload/', views.upload),
    path('login/', views.login),
    path('gallery/', views.gallery),
    path('editor/', views.editor),
]
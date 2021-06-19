from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('upload/', views.upload, name="upload"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('gallery/', views.gallery, name='gallery'),
    path('editor/', views.editor, name='editor'),
]
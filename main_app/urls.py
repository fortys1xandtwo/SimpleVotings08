"""simple_votings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('home/', home, name='home'),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('signup/', signup_view, name="signup"),
    path('vote/', vote),
    path('about/', about),
    path('voting/<str:voting>/', voting),
    path('create/', create),
    path('edit/<str:id>/', edit),
    path('profile/<str:id>/', profile),
    path('edit_profile/', edit_profile),
    path('password/', change_password),
]

"""Giveawayproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from OddamWDobreRece import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('index/', views.IndexView.as_view(), name='index'),


    path('add_donation/', views.AddDonation.as_view(), name='add_donation'),

    path('save_donation/', views.AddDonation.as_view(), name='save_donation'),
    path('save_donation1/', views.SaveCategoryInDotationSTEP1.as_view(), name='save_donation1'),
    path('save_donation2/', views.SaveCategoryInDotationSTEP2.as_view(), name='save_donation2'),
    path('save_donation3/', views.SaveCategoryInDotationSTEP3.as_view(), name='save_donation3'),
    path('save_donation4/', views.SaveCategoryInDotationSTEP4.as_view(), name='save_donation4'),
    path('form-confirmation/', views.AddDonation.as_view(), name='form-confirmation'),


    path('login/', views.LoginView.as_view(), name='login'),
    path('index/login/', views.LoginView.as_view(), name='login'),

    path('logout/', views.LogoutView.as_view(), name='logout'),


    path('register/', views.Register.as_view(), name='register'),
    path('index/register/', views.Register.as_view(), name='register'),


]

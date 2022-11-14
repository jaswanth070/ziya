"""SR URL Configuration

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
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.assistant,name='assistant'),
    # path('home',views.home,name='home'),
    # path('testing',views.test,name='testing'),
    path('assistant/',views.assistant,name='assistant'),
    path('about/',views.about,name='about'),
    path('intrest_calc/',views.intrest_calc,name='intrest_calc'),
    path('scientific_calc/',views.scientific_calc,name='scientific_calc'),
    path('percentage_calc/',views.percentage_calc,name='percentage_calc'),
    path('currency_calc/',views.currency_calc,name='currency_calc'),
    path('units_calc/',views.units_calc,name='units_calc'),
    path('contactus/',views.contactus,name='contactus'),
    path('error505/',views.error505,name='error505'),
]


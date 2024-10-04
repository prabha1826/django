"""
URL configuration for nursery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from eco.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',home,name="home"),
    path('contacts/',contacts, name="contacts"),
    path('nursery/',nursery,name="nursery"),
    path('home/',home,name="home"),
    path('admin/', admin.site.urls),
    path('plants/add/',add_plant,name="add_plant"),
    path('all/plants/',all_plants, name="all_plants"),
    path('delete/<int:plant_id>/', delete_plant, name='delete_plant'),
     path('update/<int:plant_id>/', update_plant, name='update_plant'),
     path('login/',login_page,name="login"),
     path('logout/',home,name="home"),
     path('register/',register_page,name='register'),
]

"""lcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from l1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/',views.about,name="about"),
    path('attorneys/',views.attorneys,name="attorneys"),
    path('practice-areas/',views.practice_areas,name="practice_areas"),
    path('feedback/',views.feedback,name="feedback"),
    path('register/',views.register, name="register"),
    path('u_register/', views.register, name="u_register"),
    path('login/',views.login, name="login"),
    path('practice-areas/fire/',views.fire,name="fire"),
    path('practice-areas/business/',views.business,name="business"),
    path('practice-areas/criminal/',views.criminal,name="criminal"),
    path('practice-areas/employment/',views.employment,name="employment"),
    path('practice-areas/drug/',views.drug,name="drug"),
    path('practice-areas/property/',views.proper,name="proper"),
    path('practice-areas/sexual/',views.sexual,name="sexual"),
    path('practice-areas/financial/',views.financial,name="financial"),
    path('practice-areas/insurance/',views.insurance,name="insurance"),
    path('practice-areas/family/',views.family,name="family"),

]

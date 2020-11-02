"""Edutech URL Configuration

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
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    #Functionalities
    path('', views.home, name='home'),
    path('learn/', views.learn, name='learn'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('book/', views.book, name='book'),
    path('courses/', views.courses, name='courses'),

    #class URLs
    path('class6/', views.class6, name='class6'),
    path('class7/', views.class7, name='class7'),
    path('class8/', views.class8, name='class8'),
    path('class9/', views.class9, name='class9'),
    path('class10/', views.class10, name='class10'),
    path('class11/', views.class11, name='class11'),
    path('class12/', views.class12, name='class12'),


]

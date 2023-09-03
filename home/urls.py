from django.contrib import admin
from django.urls import path, include,re_path
from home import views

urlpatterns = [
   path('',views.home, name='home'),
   path('contact', views.contact, name='contact'),
   path('about', views.about, name='about'),
   path('search', views.search, name='search'),
   path('signup', views.handleSignUp, name="handleSignUp"),
   path('login', views.handleLogin, name="handleLogin"),
   path('logout', views.handleLogout, name="handleLogout"),
]
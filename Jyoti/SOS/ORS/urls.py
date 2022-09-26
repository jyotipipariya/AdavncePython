from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.registration),

    path('log/', views.login),

    path('red/', views.red),

    path('jyoti/', views.hello),

    path('User/<int:id>/<str:name>', views.user),



]
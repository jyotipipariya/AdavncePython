from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('index/', views.index),

    path('Reg', views.registration),

    path('log/', views.login),

    path('red/', views.red),

    path('jyoti/', views.hello),

    path('User/<int:id>/<str:name>', views.user),

    path('create/', views.create_session),

    path('access/', views.access_session),

    path('destroy/', views.destroy_session),

    path("", views.auth),
    path("logout/", views.logout),
    #path('set/', views.setCookies),
    #path('get/', views.getCookies),
    path('update/', views.update),
    path('edit/<int:id>/', views.edit),
    path('dis/', views.display),


]



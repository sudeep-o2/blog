from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('register/',views.register,name='register'),
    path('upload/',views.upload,name='upload'),
    path('detail/<str:pk>',views.detailPage,name='detail'),
    path('delete/<str:pk>',views.deleteblog,name='delete'),
    path('update/<str:pk>',views.updateblog,name='update'),
]
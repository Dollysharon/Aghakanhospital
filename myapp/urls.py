
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('departments/', views.department, name='departments'),
    path('contacts/', views.contact_view, name='contacts'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>/', views.delete),
    path('showcontact/', views.showcontact, name='showcontact'),
    path('edit/<int:id>/', views.edit, name='edit'),
]




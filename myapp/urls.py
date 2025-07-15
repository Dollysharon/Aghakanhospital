
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),  # root URL
    path('home/', views.index, name='home'),
    path('starter/', views.starter, name='starter'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
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
    path('pay/', views.pay, name='pay'),

#Mpesa API URLS
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

]
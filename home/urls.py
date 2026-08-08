from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('appointment/', views.appointment, name='appointment'),
    path('billing/', views.billing, name='billing'),
    path('department/', views.department, name='department'),
]
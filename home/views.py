from django.shortcuts import render
from .models import Department, Doctors

def home(request):
    return render(request, 'home.html')
def patient(request):
    return render(request, 'patient.html')
def doctor(request):
    doctor_dic={
        'doctors':Doctors.objects.all()
    }
    return render(request, 'doctor.html', doctor_dic)

def appointment(request):
    return render(request, 'appointment.html')
def billing(request):
    return render(request, 'billing.html')
def department(request):
    dep_dic={
        'departments':Department.objects.all()
    }
    return render(request, 'department.html', dep_dic)
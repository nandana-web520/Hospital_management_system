from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()

    def __str__(self):
        return self.dep_name
class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=100)
    doc_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_phone=models.CharField(max_length=15)

    def __str__(self):
        return self.doc_name
    
class Booking(models.Model):
    patient_name=models.CharField(max_length=100)
    patient_phone=models.CharField(max_length=15)
    patient_address=models.TextField()
    patient_age=models.IntegerField()
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.patient_name
from django.db import models

# Create your models here.
class teachersrModel(models.Model):
    Name=models.CharField(null=True,max_length=100)
    Image=models.ImageField(upload_to='teacherform/')
    ContactNo=models.IntegerField()
    Emailid=models.EmailField()
    Expierence=models.IntegerField()
    teachingsubject=models.CharField(max_length=200)


class courses(models.Model):
    courseimage=models.ImageField(upload_to='imagesh/')
    coursename=models.CharField(max_length=100)
    courseduration=models.CharField(max_length=60)
    coursedetails=models.CharField(max_length=300)
    coursefee=models.DecimalField(max_digits=7,decimal_places=2)

class studentsrModel(models.Model):
    Name=models.CharField(null=True,max_length=100)
    Image=models.ImageField(upload_to='teacherform/')
    ParentNo=models.IntegerField()
    Branch=models.CharField(max_length=40)
    Section=models.CharField(max_length=40)
    Subjects=models.CharField(max_length=200)
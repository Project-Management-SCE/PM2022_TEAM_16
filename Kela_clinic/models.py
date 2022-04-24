from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class PatientModel(models.Model):
    ID=models.CharField(db_column='ID',max_length=9,primary_key=True)
    firstname=models.TextField(db_column='firstname')
    lastname=models.TextField(db_column='lastname')
    password=models.CharField(db_column='password',max_length=10)
    messagesent=models.TextField(db_column='messagesent')
    DIC=models.CharField(db_column='DID',max_length=9)
    medicalrecod=models.TextField(db_column='medicalrecod')
  

    def patient_update_status(user):
        all_status = ["sick","very sick","healthy"]
        if user!= None or user.status!="healthy" and user.status in all_status:
            user.status = all_status[all_status.index(user.status) + 1]
            return "status of user {0} update seucces".format(user.firstname)
        return "status of user {0} update not seucces".format(user.firstname)


    class Meta:
        managed = False
        db_table = 'user'

class DoctorModel(models.Model):
    ID=models.CharField(db_column='ID',max_length=9,primary_key=True)
    firstname=models.TextField(db_column='firstname')
    lastname=models.TextField(db_column='lastname')
    password=models.CharField(db_column='password',max_length=10)
    patientID=models.CharField(db_column='PID',max_length=9)
    workday=models.TextField(db_column='workday')

    def get_all_madicl():
       return [
           "Methylphenidate Hydrochloride",
           "Glimepiride",
           "Methocarbamol",
           "Acetaminophen",
           "Oasis TEARS PLUS",
           "Selenium",
           "Calcium Acetate"
           "entresto",
           "Etodolac",
           "Ciclosporin",
           "Lithium Bromatum",
           "Flovent Diskus",
           "Methyldopa",
           "Tazorac",
           "Linezolid",
           "Losartan",
           "ciprofloxacin"
           "Amlodipine"
           "Eszopiclone",
            ]

    class Meta:
        managed = False
        db_table = 'doctor'


class Adminmodel(models.Model):
    ID=models.CharField(db_column='ID',max_length=9,primary_key=True)
    firstname=models.TextField(db_column='firstname')
    lastname=models.TextField(db_column='lastname')
    password=models.CharField(db_column='password',max_length=10)
    messagesent=models.TextField(db_column='messagesent')
    class Meta:
        managed = False
        db_table = 'admin'



class MessageModel(models.Model):
    ID=models.CharField(db_column='ID',max_length=9,primary_key=True)
    message=models.TextField(db_column='message')
    class Meta:
        managed = False
        db_table = 'generalmessage'       
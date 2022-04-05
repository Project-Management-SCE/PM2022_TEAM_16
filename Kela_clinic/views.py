from random import random
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from Kela_clinic.models import *
import mysql.connector
from django.http import JsonResponse
import random
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# Create your views here.

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database=" projectapp"
)
cursor = db_connection.cursor()
print(db_connection)

# START PAGE WITH ANIMATION
mess=MessageModel.objects.filter(ID=1)

def index(request):
    return render(request, 'customers/homepage.html')


def userlogin(request):
    return render(request, 'customers/loginpage.html')

#login functions###############################
def login(request):
    return render(request, 'doctors/loginpage.html')

def userdash(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        print(ID,password)
        PatientModel1 = PatientModel.objects.filter(ID=ID, password=password)
        if PatientModel1:
            return render(request, 'customers/dash.html', {"PatientModel": PatientModel1})  

def workersdash(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID, password=password)
        PatientModel1 = PatientModel.objects.filter(DIC=ID)
        Adminmodel1 = Adminmodel.objects.filter(ID=ID, password=password)
        print(PatientModel1)
        if DoctorModel1:
            return render(request, 'doctors/dash.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1})  
        elif Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall })  
#######################################################################################################################################
def fichinfo(request):
    if request.method == 'POST':
        Fichinfo = request.POST.get('FID')
        ID = request.POST.get('ID')   
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        PatientModel1 = PatientModel.objects.filter(ID=Fichinfo)
        DoctorModel1 = DoctorModel.objects.filter(ID=Fichinfo)
        if DoctorModel1:
          return render(request, 'admin/ficheinfodoc.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModel1, "message":mess})  
        elif  PatientModel1:     
          return render(request, 'admin/ficheinfopatient.html', {"AdminModel": Adminmodel1, "PatientModel":PatientModel1, "message":mess })

def doctest(request):
    test = DoctorModel.objects.filter(ID='111222333').first()
    workday2=test.workday
    x = workday2.split(",")
    print(x[1])

def addmedicalrecord(request):
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DID')
        messages = request.POST.get('message')
        print(PID,DID,messages)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID).first()
        mes=PatientModel1.medicalrecod
        medrecord=messages+" "+mes+" "
        PatientModel2 = PatientModel.objects.filter(ID=PID)
        cursor.execute("UPDATE `user` SET `medicalrecod` = '%s' WHERE `user`.`ID` = '%s';"%(medrecord,PID))
        db_connection.commit()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel2, "message":mess})  




def sentmessage(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        if PatientModel1:
            return render(request, 'customers/messagesent.html', {"PatientModel": PatientModel1, "message":mess})  

def patientpage(request):
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DIC')
        print(PID,DID)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID)
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess})  

def patientsending(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        reason = request.POST.get('reason')
        urgent = request.POST.get('urgent')
        message = request.POST.get('message')
        TO = request.POST.get('TO')
        if TO=='My doctor':
            messagetodoc='Reason:'+reason+'\n Message:'+message
            cursor.execute("UPDATE `user` SET `messagesent` = '%s' WHERE `user`.`ID` = '%s';"%(messagetodoc,ID))
            db_connection.commit()
        elif TO=='The Manager':
            messagetodoc='Reason:'+reason+'\n Message:'+message
            cursor.execute("UPDATE `user` SET `adminmess` = '%s' WHERE `user`.`ID` = '%s';"%(messagetodoc,ID))
            db_connection.commit()
        print(reason,urgent,message)
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        if PatientModel1:
            return render(request, 'customers/dash.html', {"PatientModel": PatientModel1, "message":mess}) 

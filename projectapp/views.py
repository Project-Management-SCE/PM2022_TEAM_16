from random import random
from tkinter import Frame
from cv2 import COLOR_BGR2GRAY, destroyAllWindows
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from projectapp.models import *
import mysql.connector
from django.http import JsonResponse
import random
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import numpy as np
import cv2
import pickle
from django.core.files.storage import FileSystemStorage
import requests
import json
# Create your views here.
import time

db_connection = mysql.connector.connect(
    host="database-1.cx6ixgbmnqky.eu-central-1.rds.amazonaws.com",
    user="Admin",
    password="Aa123456",
    database="projectapp"
)
cursor = db_connection.cursor()
print(db_connection)
# START PAGE WITH ANIMATION
"""
medsnames =  ["Methylphenidate Hydrochloride",
                "Glimepiride",
                "Methocarbamol",
                "Acetaminophen",
                "Oasis TEARS PLUS",
                "Selenium",
                "Calcium Acetate",
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
                ]   
Warn=[]
for med in medsnames:
            path = "https://api.fda.gov/drug/label.json?search=" + med
            response = requests.get(path)
            js = response.json()["results"]
            contect_medical = js[0]
            WARNINGS  = ""
            if 'boxed_warning' in contect_medical:
                WARNINGS = contect_medical["boxed_warning"]
            elif 'warnings' in contect_medical:
                WARNINGS = contect_medical["warnings"]
            else:
                WARNINGS = contect_medical["warnings_and_cautions"]
            if len(WARNINGS)>1:
                Warn.append(WARNINGS[0])
            else:
                Warn+=WARNINGS
zip_iterator = zip(medsnames, Warn)
a_dictionary = dict(zip_iterator)
"""
a_dictionary={1:1}
print(a_dictionary)

def index(request):
    return render(request, 'customers/homepage.html')

def newcust(request):
    if request.method == 'POST':
        firstname1 = request.POST.get('firstname')
        lastname1 = request.POST.get('lastname')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        print(firstname1,lastname1,email1,phone1)
        saveobject=newcustomerModel()
        saveobject.firstname=firstname1
        saveobject.lastname=lastname1
        saveobject.email=email1
        saveobject.phone=phone1
        saveobject.save()
        return render(request, 'customers/homepage.html')

def userlogin(request):
    return render(request, 'customers/loginpage.html')

#login functions###############################
def login(request):
    return render(request, 'doctors/loginpage.html')

def userdash(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        print(ID,password)
        PatientModel1 = PatientModel.objects.filter(ID=ID, password=password)
        PatientModeltest = PatientModel.objects.filter(ID=ID, password=password).first()
        DID=PatientModeltest.DID
        DoctorModel3 = DoctorModel.objects.filter(ID=DID).first()
        print(DoctorModel3)
        workday2=DoctorModel3.workdays
        print(workday2)
        x = workday2.split(",")
        dictOfWords = { i : 10 for i in x }
        meds = PatientModeltest.medrecom.split(",")
        dictOfWords1 = { i : 10 for i in meds }
        hours=['10:00','10:30','11:00','11:30','12:00','12:30','13:00']
        dichours = { i : 10 for i in hours }
        print(dictOfWords) 
        if PatientModel1:
            return render(request, 'customers/dash.html', {"PatientModel": PatientModel1, "message":mess,'dictOfWords':dictOfWords,'medslist':dictOfWords1,"dichours":dichours})  
        else:
            return render(request, 'customers/loginpage.html')
    else:
        return render(request, 'customers/loginpage.html')
def userdashbutton(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        PatientModeltest = PatientModel.objects.filter(ID=ID).first()
        DID=PatientModeltest.DID
        DoctorModel3 = DoctorModel.objects.filter(ID=DID).first()
        print(DoctorModel3)
        workday2=DoctorModel3.workdays
        print(workday2)
        x = workday2.split(",")
        workday = { i : 10 for i in x }
        meds = PatientModeltest.medrecom.split(",")
        dictOfWords1 = { i : 10 for i in meds }
        hours=['10:00','10:30','11:00','11:30','12:00','12:30','13:00']
        dichours = { i : 10 for i in hours }
        print(workday) 
        if PatientModel1:
            return render(request, 'customers/dash.html', {"PatientModel": PatientModel1, "message":mess,'dictOfWords':workday,'medslist':dictOfWords1,"dichours":dichours})  

def rdv(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('CID')
        day=request.POST.get('Cday')
        hour=request.POST.get('hour')
        print(ID,day)
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        PatientModeltest = PatientModel.objects.filter(ID=ID).first()
        DID=PatientModeltest.DID
        DoctorModel3 = DoctorModel.objects.filter(ID=DID).first()
        print(DoctorModel3)
        workday2=DoctorModel3.workdays
        print(workday2)
        x = workday2.split(",")
        dictOfWords = { i : 10 for i in x }
        meds = PatientModeltest.medrecom.split(",")
        dictOfWords1 = { i : 10 for i in meds }
        hours=['10:00','10:30','11:00','11:30','12:00','12:30','13:00']
        dichours = { i : 10 for i in hours }
        app=day+" "+hour
        cursor.execute("UPDATE `user` SET `appointement` = '%s' WHERE `user`.`ID` = '%s';"%(app,ID))
        db_connection.commit()
        print(dictOfWords) 
        if PatientModel1:
            return render(request, 'customers/dash.html', {"PatientModel": PatientModel1, "message":mess,'dictOfWords':dictOfWords,'medslist':dictOfWords1,'dichours':dichours}) 

def doctorinfo(request):
    mess=MessageModel.objects.filter(ID=1)
    allmed=MedsModel.objects.all()
    if request.method == 'POST':
        ID = request.POST.get('ID')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        if DoctorModel1:
                return render(request, 'doctors/privateinfo.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':allmed})


def workersdash(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID, password=password)
        PatientModel1 = PatientModel.objects.filter(DID=ID)
        Adminmodel1 = Adminmodel.objects.filter(ID=ID, password=password)
        print(PatientModel1)
        if DoctorModel1:
            return render(request, 'doctors/dash.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess})  
        elif Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            PatientModelall= PatientModel.objects.all()
            newcustomerModelall = newcustomerModel.objects.all()
            return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess,'newcustomerModel':newcustomerModelall })
        else:
            return render(request, 'doctors/loginpage.html')
    else:
        return render(request, 'doctors/loginpage.html')      

def dochomebut(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        PatientModel1 = PatientModel.objects.filter(DID=ID)
        print(PatientModel1)
        if DoctorModel1:
            return render(request, 'doctors/dash.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess})  

def adminpharmacy(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        allmed=MedsModel.objects.all()      
        return render(request, 'admin/pharmacygest.html', {"AdminModel": Adminmodel1, "message":mess, 'meds':allmed})

def addmeds(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        allmed=MedsModel.objects.all()      
        return render(request, 'admin/addmeds.html', {"AdminModel": Adminmodel1, "message":mess, 'meds':allmed})

def addmed(request):
    #add new medical
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST' and request.FILES['myfile']:
        ID = request.POST.get('AID')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        pstock = request.POST.get('pstock')
        estock = request.POST.get('estock')
        reason= request.POST.get('reason')
        saveobj=MedsModel()
        saveobj.name=name
        saveobj.description=description
        saveobj.price=price
        saveobj.pstock=pstock
        saveobj.estock=estock
        saveobj.reason=reason
        saveobj.save()
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save('C:\\Users\\kevyn\\Happysammy\\projectapp\\static\\pharmacieimg\\18.jpg', myfile)
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        allmed=MedsModel.objects.all()      
        return render(request, 'admin/addmeds.html', {"AdminModel": Adminmodel1, "message":mess, 'meds':allmed})


def adminmedinfo(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('DID')
        MID = request.POST.get('MID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        MedsModel1 = MedsModel.objects.filter(ID=MID)
        samemeds=MedsModel.objects.filter(ID=MID).first()
        samemedsreason=samemeds.reason
        MedsModelR = MedsModel.objects.filter(reason=samemedsreason)
        if Adminmodel1 and MedsModel1 :
            return render(request, 'admin/medinfo.html', {"Adminmodel": Adminmodel1, "message":mess, 'meds':MedsModel1,'meds2':MedsModelR,"a_dictionary":a_dictionary})

def medchange(request):
    #change quantities remove med
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('AID')
        MID = request.POST.get('MID')
        estock = request.POST.get('estock')
        pstock = request.POST.get('pstock')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        MedsModel1 = MedsModel.objects.filter(ID=MID)
        cursor.execute("UPDATE `meds` SET `estock` = '%s' WHERE `meds`.`ID` = '%s';"%(estock,MID))
        db_connection.commit()
        cursor.execute("UPDATE `meds` SET `pstock` = '%s' WHERE `meds`.`ID` = '%s';"%(pstock,MID))
        db_connection.commit()
        samemeds=MedsModel.objects.filter(ID=MID).first()
        samemedsreason=samemeds.reason
        MedsModelR = MedsModel.objects.filter(reason=samemedsreason)
        if Adminmodel1 and MedsModel1 :
            return render(request, 'admin/medinfo.html', {"Adminmodel": Adminmodel1, "message":mess, 'meds':MedsModel1,'meds2':MedsModelR,"a_dictionary":a_dictionary})    

def addpatpage(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        NID = request.POST.get('NID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        newcustomerModel1 = newcustomerModel.objects.filter(phone=NID)
        print(Adminmodel1)
        if Adminmodel1:
            return render(request, 'admin/addpat.html', {"Adminmodel":Adminmodel1,"message":mess,'newcustomerModel':newcustomerModel1})  

def adddocpage(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        print(Adminmodel1)
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            return render(request, 'admin/adddoc.html', {"Adminmodel":Adminmodel1,"message":mess,"DoctorModel":DoctorModelall}) 

def adddoctor(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        AID = request.POST.get('AID')
        ID = request.POST.get('ID')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        speciality = request.POST.get('spec')
        password='Aa123456'
        saveobj=DoctorModel()
        saveobj.ID=ID
        saveobj.firstname=firstname
        saveobj.lastname=lastname
        saveobj.speciality=speciality
        saveobj.password=password
        saveobj.workdays=None
        saveobj.adminmess=None
        saveobj.adminanswer=None
        saveobj.save()
        Adminmodel1 = Adminmodel.objects.filter(ID=AID)
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            return render(request, 'admin/adddoc.html', {"Adminmodel":Adminmodel1,"message":mess,"DoctorModel":DoctorModelall}) 

def deletedoc(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        DID = request.POST.get('DID')
        ID = request.POST.get('ID')    
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        cursor.execute("DELETE FROM `doctor` WHERE `doctor`.`ID` = '%s';"%(DID))
        db_connection.commit()
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            return render(request, 'admin/adddoc.html', {"Adminmodel":Adminmodel1,"message":mess,"DoctorModel":DoctorModelall}) 

def allMedsdoc(request):   
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        type = request.POST.get('type')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        Painkillers = MedsModel.objects.filter(type='painkiller')
        Narco = MedsModel.objects.filter(type='narcoleptics')
        pastes = MedsModel.objects.filter(type='pastes')
        cold = MedsModel.objects.filter(type='anti-cold mecicine')
        allmed=MedsModel.objects.all()      
        if DoctorModel1:
            if type=='painkiller':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':Painkillers})  
            if type=='narcoleptics':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':Narco})
            if type=='pastes':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':pastes})                
            if type=='anti-cold mecicine':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':cold})
            if type=='all':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':allmed})

  
#######################################################################################################################################
def medinfo(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('DID')
        MID = request.POST.get('MID')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        MedsModel1 = MedsModel.objects.filter(ID=MID)
        samemeds=MedsModel.objects.filter(ID=MID).first()
        samemedsreason=samemeds.reason
        MedsModelR = MedsModel.objects.filter(reason=samemedsreason)
        if DoctorModel1 and MedsModel1 :
            return render(request, 'doctors/medinfo.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':MedsModel1,'meds2':MedsModelR,"a_dictionary":a_dictionary})
def pharmacybutton(request):    
    allmed=MedsModel.objects.all()
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        PatientModeltest = PatientModel.objects.filter(ID=ID).first()
        if PatientModel1:
            meds = PatientModeltest.medrecom.split(",")
            dictOfWords1 = { i : 10 for i in meds } 
            return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,'medslist':dictOfWords1})        
             
def fichinfo(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        Fichinfo = request.POST.get('FID')
        ID = request.POST.get('ID')   
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        PatientModel1 = PatientModel.objects.filter(ID=Fichinfo)
        DoctorModel1 = DoctorModel.objects.filter(ID=Fichinfo)
        if DoctorModel1:
          return render(request, 'admin/ficheinfodoc.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModel1, "message":mess})  
        elif  PatientModel1:
            PatientModel2 = PatientModel.objects.filter(ID=Fichinfo).first()
            DID=PatientModel2.DID
            DoctorModel1 = DoctorModel.objects.filter(ID=DID)
            return render(request, 'admin/ficheinfopatient.html', {"AdminModel": Adminmodel1, "PatientModel":PatientModel1,"DoctorModel":DoctorModel1, "message":mess })

# Add Medical Record
def addmedicalrecord(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DID')
        messages = request.POST.get('message')
        print(PID,DID,messages)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID).first()
        mes=PatientModel1.medicalrecord
        medrecord=messages+" "+mes+" "
        PatientModel2 = PatientModel.objects.filter(ID=PID)
        cursor.execute("UPDATE `user` SET `medicalrecord` = '%s' WHERE `user`.`ID` = '%s';"%(medrecord,PID))
        db_connection.commit()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel2, "message":mess})  

def logout(request):
    return render(request, 'doctors/loginpage.html')


def addmedicalrecomandation(request):
    #doctor send drug recomandation
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DID')
        messages = request.POST.get('message')
        print(PID,DID,messages)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID).first()
        mes=PatientModel1.medrecom
        addmeds=mes+','+messages
        PatientModel2 = PatientModel.objects.filter(ID=PID)
        cursor.execute("UPDATE `user` SET `medrecom` = '%s' WHERE `user`.`ID` = '%s';"%(addmeds,PID))
        db_connection.commit()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel2, "message":mess})  
def adminanswer(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        AID = request.POST.get('AID')
        PID = request.POST.get('PID')
        message = request.POST.get('message')
        cursor.execute("UPDATE `user` SET `adminanswer` = '%s' WHERE `user`.`ID` = '%s';"%(message,PID))
        db_connection.commit()
        Adminmodel1 = Adminmodel.objects.filter(ID=AID)
        PatientModel1 = PatientModel.objects.filter(ID=PID)
        PatientModel2 = PatientModel.objects.filter(ID=PID).first()
        DID=PatientModel2.DID
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        return render(request, 'admin/ficheinfopatient.html', {"AdminModel": Adminmodel1, "PatientModel":PatientModel1,"DoctorModel":DoctorModel1, "message":mess })

def autorization(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        AID = request.POST.get('AID')
        PID = request.POST.get('PID')
        message = request.POST.get('autor')
        cursor.execute("UPDATE `user` SET `autorizations` = '%s' WHERE `user`.`ID` = '%s';"%(message,PID))
        db_connection.commit()
        Adminmodel1 = Adminmodel.objects.filter(ID=AID)
        PatientModel1 = PatientModel.objects.filter(ID=PID)
        PatientModel2 = PatientModel.objects.filter(ID=PID).first()
        DID=PatientModel2.DID
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        return render(request, 'admin/ficheinfopatient.html', {"AdminModel": Adminmodel1, "PatientModel":PatientModel1,"DoctorModel":DoctorModel1, "message":mess })

def admintodoc(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        AID = request.POST.get('ID')
        DID = request.POST.get('DID')
        message = request.POST.get('message')
        cursor.execute("UPDATE `doctor` SET `adminanswer` = '%s' WHERE `doctor`.`ID` = '%s';"%(message,DID))
        db_connection.commit()
        Adminmodel1 = Adminmodel.objects.filter(ID=AID)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        return render(request, 'admin/ficheinfodoc.html', {"AdminModel": Adminmodel1, "DoctorModel":DoctorModel1, "message":mess })

def addprivaterecord(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DID')
        messages = request.POST.get('message')
        print(PID,DID,messages)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID).first()
        PatientModel2 = PatientModel.objects.filter(ID=PID)
        mess=PatientModel1.privaterecord
        add= messages+" "+mess
        cursor.execute("UPDATE `user` SET `privaterecord` = '%s' WHERE `user`.`ID` = '%s';"%(add,PID))
        db_connection.commit()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel2, "message":mess})  

def sentmessage(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        if PatientModel1:
            return render(request, 'customers/messagesent.html', {"PatientModel": PatientModel1, "message":mess})  

def patientpage(request):
    #personal patient page for doctor
    #patients model page
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DIC')
        print(PID,DID)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID)
        #display data of patients
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess})  

def patientsending(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        reason = request.POST.get('reason')
        urgent = request.POST.get('urgent')
        message = request.POST.get('message')
        PatientModel1 = PatientModel.objects.filter(ID=ID).first()
        messagetodoc='Urgent:'+urgent+' \n Reason:'+reason+'\n Message:'+message
        medrecord= "\n "+messagetodoc+" "
        print(medrecord)
        TO = request.POST.get('TO')
        if TO=='My doctor':
            cursor.execute("UPDATE `user` SET `messagesent` = '%s' WHERE `user`.`ID` = '%s';"%(messagetodoc,ID))
            db_connection.commit()
        elif TO=='The Manager':
            messagetodoc='Reason:'+reason+'\n Message:'+message
            cursor.execute("UPDATE `user` SET `adminmess` = '%s' WHERE `user`.`ID` = '%s';"%(messagetodoc,ID))
            db_connection.commit()
        print(reason,urgent,message)
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        if PatientModel1:
            return render(request, 'customers/messagesent.html', {"PatientModel": PatientModel1, "message":mess}) 


def doctoranswer(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PAT')
        DID = request.POST.get('DID')
        reason = request.POST.get('reason')
        message = request.POST.get('message')
        messagefromdoc= 'Reason:'+reason+'Message:'+message
        cursor.execute("UPDATE `user` SET `doctoranswer` = '%s' WHERE `user`.`ID` = '%s';"%(messagefromdoc,PID))
        db_connection.commit()
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID)
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess})  

def genmessage(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        message = request.POST.get('message')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID) 
        mesID='1'
        cursor.execute("UPDATE `generalmessage` SET `message` = '%s' WHERE `generalmessage`.`ID` = '%s';"%(message,mesID))
        db_connection.commit()
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            PatientModelall= PatientModel.objects.all()
            return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess }) 

def adminsentmess(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        reason = request.POST.get('reason')
        message = request.POST.get('message')
        TO = request.POST.get('TO')
        #if TO=='doctor':
           # messagetodoc='Urgent:'+urgent+' \n Reason:'+reason+'\n Message:'+message
           # cursor.execute("UPDATE `user` SET `messagesent` = '%s' WHERE `user`.`ID` = '%s';"%(messagetodoc,ID))
           # db_connection.commit()
        if TO=='The Manager':
            messagetoman='Reason:'+reason+'\n Message:'+message
            cursor.execute("UPDATE `doctor` SET `adminmess` = '%s' WHERE `doctor`.`ID` = '%s';"%(messagetoman,ID))
            db_connection.commit()
        print(reason,message)
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        PatientModel1 = PatientModel.objects.filter(DID=ID)
        print(PatientModel1)
        if DoctorModel1:
            return render(request, 'doctors/dash.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess})  


def checkout(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        CID = request.POST.get('CID')
        cursor.execute("DELETE FROM `customercart` WHERE `customercart`.`CID` = '%s';"%(CID))
        db_connection.commit()
        PatientModel1 = PatientModel.objects.filter(ID=CID)
        return render(request, 'customers/checkout.html',{"PatientModel":PatientModel1})
#############################################################################################################################################################################


def addcart(request):
    allmed=MedsModel.objects.all()
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        CID = request.POST.get('CID') 
        MID = request.POST.get('MID')
        NAME = request.POST.get('NAME')
        CommandeenCour = cartModel.objects.filter(CID=CID)
        PatientModel1 = PatientModel.objects.filter(ID=CID)
        PatientModeltest = PatientModel.objects.filter(ID=CID).first()
        pname=PatientModeltest.firstname
        CommandeenCour1 = cartModel.objects.filter(CID=CID).first()
        Medic = MedsModel.objects.filter(ID=MID).first()
        if Medic.type=='narcoleptics':
            if PatientModeltest.autorization=='no':
                    face_cascade = cv2.CascadeClassifier('C:\\Users\\kevyn\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
                    recognizer = cv2.face.LBPHFaceRecognizer_create() 
                    recognizer.read("C:\\Users\\kevyn\\Happysammy\\projectapp\\trainner.yml")
                    labels = {}
                    with open("C:\\Users\\kevyn\\Happysammy\\projectapp\\labels.pickle", "rb") as f :
                        og_labels = pickle.load(f)
                        labels = {v:k for k,v in og_labels.items()}
                    cap = cv2.VideoCapture(0)
                    while(True):
                        ret,frame= cap.read()
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
                        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5,minNeighbors=5)
                        for(x,y,w,h) in faces:
                            #print(x,y,w,h)
                            roi_gray= gray[y:y+h ,x:x+w]
                            roi_color = frame[y:y+h ,x:x+w]
                            id_,conf = recognizer.predict(roi_gray)
                            if conf >= 45 or conf < 85 :
                                #print(id_)
                                #print(labels[id_])
                                font = cv2.FONT_HERSHEY_SIMPLEX
                                name = labels[id_]
                                color = (255,255,255)
                                stroke= 2
                            cv2.putText(frame,name,(x+1,y+1),font,2,color, stroke, cv2.LINE_AA)
                            # use recognize
                            color = (250,0,0)
                            stroke=5
                            end_cord_x = x+w
                            end_cord_y = y + h 
                            cv2.rectangle(frame, (x,y),(end_cord_x,end_cord_y), color,stroke) #dessign le rectagle  
                            cv2.imshow('Autentificator 2000!',frame) 
                            if pname==name or cv2.waitKey(20) & 0xFF == ord('q'):
                                cv2.imshow('Autentificator 2000!',frame)
                                prixmed=Medic.price
                                if CommandeenCour:          
                                    listmedoc=CommandeenCour1.MIDS+','+MID
                                    prixajouter=CommandeenCour1.totalprice+prixmed
                                    names=CommandeenCour1.name+','+NAME
                                    cursor.execute("UPDATE `customercart` SET `totalprice` = '%s' WHERE `customercart`.`CID` = '%s';"%(prixajouter,CID))
                                    db_connection.commit()
                                    cursor.execute("UPDATE `customercart` SET `MIDS` = '%s' WHERE `customercart`.`CID` = '%s';"%(listmedoc,CID))
                                    db_connection.commit()
                                    cursor.execute("UPDATE `customercart` SET `name` = '%s' WHERE `customercart`.`CID` = '%s';"%(names,CID))
                                    db_connection.commit()
                                    x = names.split(",")
                                    dictOfWords = { i : 10 for i in x }
                                    meds = PatientModeltest.medrecom.split(",")
                                    dictOfWords1 = { i : 10 for i in meds }
                                    print(dictOfWords1)                    
                                    cap.release()
                                    cv2.destroyAllWindows()
                                    return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,"CommandeenCour":dictOfWords,"medslist":dictOfWords1})
                                else:
                                    saveobject=cartModel()
                                    print(NAME)
                                    saveobject.CID=CID
                                    saveobject.MIDS=MID
                                    saveobject.totalprice=prixmed
                                    saveobject.name=NAME
                                    saveobject.save()
                                    CommandeenCour2 = cartModel.objects.filter(CID=CID)
                                                        
                                    cap.release()
                                    cv2.destroyAllWindows()
                                    return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,"CommandeenCour":CommandeenCour2})
        prixmed=Medic.price
        if CommandeenCour:          
          listmedoc=CommandeenCour1.MIDS+','+MID
          prixajouter=CommandeenCour1.totalprice+prixmed
          names=CommandeenCour1.name+','+NAME
          cursor.execute("UPDATE `customercart` SET `totalprice` = '%s' WHERE `customercart`.`CID` = '%s';"%(prixajouter,CID))
          db_connection.commit()
          cursor.execute("UPDATE `customercart` SET `MIDS` = '%s' WHERE `customercart`.`CID` = '%s';"%(listmedoc,CID))
          db_connection.commit()
          cursor.execute("UPDATE `customercart` SET `name` = '%s' WHERE `customercart`.`CID` = '%s';"%(names,CID))
          db_connection.commit()
          x = names.split(",")
          dictOfWords = { i : 10 for i in x }
          meds = PatientModeltest.medrecom.split(",")
          dictOfWords1 = { i : 10 for i in meds }
          print(dictOfWords1)
          return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,"CommandeenCour":dictOfWords,"medslist":dictOfWords1})
        else:
            saveobject=cartModel()
            print(NAME)
            saveobject.CID=CID
            saveobject.MIDS=MID
            saveobject.totalprice=prixmed
            saveobject.name=NAME
            saveobject.save()
            CommandeenCour2 = cartModel.objects.filter(CID=CID)
            return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,"CommandeenCour":CommandeenCour2})

def admintodocworkday(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        DID = request.POST.get('DID')
        print(DID)
        ID = request.POST.get('ID')
        print(ID)
        workdays = request.POST.get('days')
        print(workdays)
        cursor.execute("UPDATE `doctor` SET `workday` = '%s' WHERE `doctor`.`ID` = '%s';"%(workdays,DID))
        db_connection.commit()
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        print(Adminmodel1)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        return render(request, 'admin/ficheinfodoc.html', {"AdminModel": Adminmodel1, "DoctorModel":DoctorModel1, "message":mess })

def pay(request):
    allmed=MedsModel.objects.all()
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        CID = request.POST.get('CID') 
        CommandeenCour = cartModel.objects.filter(CID=CID)
        CommandeenCour1 = cartModel.objects.filter(CID=CID).first()
        x = CommandeenCour1.name.split(",")
        res = {i:x.count(i) for i in x}
        dictOfWords = { i : 10 for i in x }
        total=CommandeenCour1.totalprice
        dic = {total:1}
        PatientModel1 = PatientModel.objects.filter(ID=CID)
        print(res)
        return render(request, 'customers/resumercomande.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"CommandeenCour":CommandeenCour,'res':res,'dic':dic})




def payement(request):
    allmed=MedsModel.objects.all()
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        CID = request.POST.get('CID') 
        print(CID)
        CommandeenCour1 = cartModel.objects.filter(CID=CID)
        return render(request, 'customers/pay.html',{"CommandeenCour":CommandeenCour1})
 ###########################################################################################################################################################################           

def testcam(request):
    mess=MessageModel.objects.filter(ID=1)
    face_cascade = cv2.CascadeClassifier('C:\\Users\\kevyn\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    recognizer.read("C:\\Users\\kevyn\\Happysammy\\projectapp\\trainner.yml")
    labels = {}
    with open("C:\\Users\\kevyn\\Happysammy\\projectapp\\labels.pickle", "rb") as f :
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    cap = cv2.VideoCapture(0)
    while(True):
        ret,frame= cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5,minNeighbors=5)
        for(x,y,w,h) in faces:
            #print(x,y,w,h)
            roi_gray= gray[y:y+h ,x:x+w]
            roi_color = frame[y:y+h ,x:x+w]
            id_,conf = recognizer.predict(roi_gray)
            if conf >= 45 or conf < 85 :
                #print(id_)
                #print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                name2=name
                color = (255,255,255)
                stroke= 2
            cv2.putText(frame,name,(x+1,y+1),font,2,color, stroke, cv2.LINE_AA)
            # use recognize
            color = (250,0,0)
            stroke=5
            end_cord_x = x+w
            end_cord_y = y + h 
            cv2.rectangle(frame, (x,y),(end_cord_x,end_cord_y), color,stroke) #dessign le rectagle
        cv2.imshow('Autentificator 2000!',frame)
        #print(name2)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        #if name1==name2:
        #    name4='kevyn'
        #    PatientModel1 = PatientModel.objects.filter(firstname=name4)
        #    return render(request, 'customers/dash.html',{"PatientModel": PatientModel1})
# When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


    med1='ciprofloxacin'
    path = "https://api.fda.gov/drug/label.json?search=" + med1
    response = requests.get(path)
    js = response.json()["results"]
    contect_medical = js[0]
    WARNINGS  = ""
    if 'boxed_warning' in contect_medical:
            WARNINGS = contect_medical["boxed_warning"]
    elif 'warnings' in contect_medical:
        WARNINGS = contect_medical["warnings"]
    else:
        WARNINGS = contect_medical["warnings_and_cautions"]


    test={'test':WARNINGS}

all_med =  ["ciprofloxacin",
            "Losartan",
            "Linezolid",
            "Ofloxacin",
            "MEKINIST",
            "Methylphenidate Hydrochloride",
            "Glimepiride",
            "Methocarbamol",
            "Acetaminophen",
            "Oasis TEARS PLUS",
            "Selenium",
            "Calcium Acetate",
            "entresto",
            "Etodolac",
            "Ciclosporin",
            "Lithium Bromatum",
            "Flovent Diskus",
            "Methyldopa",
             "Tazorac"
            ]

med1='Losartan'
path = "https://api.fda.gov/drug/label.json?search=" + med1
response = requests.get(path)
js = response.json()["results"]
contect_medical = js[0]
WARNINGS  = ""
if 'boxed_warning' in contect_medical:
    WARNINGS = contect_medical["boxed_warning"]
elif 'warnings' in contect_medical:
    WARNINGS = contect_medical["warnings"]
else:
    WARNINGS = contect_medical["warnings_and_cautions"]



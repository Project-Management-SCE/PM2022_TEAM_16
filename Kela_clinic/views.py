from random import random
from tkinter import Frame
from cv2 import COLOR_BGR2GRAY, destroyAllWindows
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
import numpy as np
import cv2
import pickle
# Create your views here.

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database=" projectapp"
)
cursor = db_connection.cursor()
print(db_connection)

# START PAGE WITH ANIMATION

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

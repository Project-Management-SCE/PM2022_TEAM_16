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

def index(request):
    return render(request, 'customers/homepage.html')


def userlogin(request):
    return render(request, 'customers/loginpage.html')
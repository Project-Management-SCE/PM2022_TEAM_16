from django.test import TestCase
from django.urls import resolve, reverse
from projectapp.views import *
from projectapp.models import Adminmodel
import unittest

class TestUrls(unittest.TestCase):

    def test_list_url_is_resolved(self):
        url=reverse('index')
        print(resolve(url))

''''
class test_admin(TestCase):
    def test_admin1(self):
        item=Adminmodel()
        item.ID='315199059'
        item.firstname='Lior'
        item.lastname='Liberov'
        item.password='1a2b3c4d5e'
        item.messagesent='hello world'
        item.save()
        record=Adminmodel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)
    
    def test_admin2(self):
        item=Adminmodel()
        item.ID='324561087'
        item.firstname='Jack'
        item.lastname='Maori'
        item.password='8888855555'
        item.messagesent='hello world'
        item.save()
        record=Adminmodel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_admin3(self):
        item=Adminmodel()
        item.ID='324561056'
        item.firstname='Matan'
        item.lastname='Tariff'
        item.password='8888844444'
        item.messagesent='hello world'
        item.save()
        record=Adminmodel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

class doctor_test(TestCase):
    def test_doctor1(self):
        item=DoctorModel()
        item.ID='324461056'
        item.firstname='Alex'
        item.lastname='Yohananoff'
        item.password='1234567890'
        item.patientID='324561156'
        item.workday='23/4/22'
        item.save()
        record=DoctorModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)
    
    def test_doctor2(self):
        item=DoctorModel()
        item.ID='324561056'
        item.firstname='John'
        item.lastname='Elbaz'
        item.password='1234567790'
        item.patientID='324561256'
        item.workday='24/4/22'
        item.save()
        record=DoctorModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_doctor3(self):
        item=DoctorModel()
        item.ID='324661056'
        item.firstname='Mark'
        item.lastname='Efraim'
        item.password='1234467890'
        item.patientID='324561356'
        item.workday='26/4/22'
        item.save()
        record=DoctorModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

class patient_test(TestCase):
    def test_patient1(self):
        item=PatientModel()
        item.ID='324561156'
        item.firstname='Matan'
        item.lastname='Gershon'
        item.password='1234567890'
        item.messagesent='hello world'
        item.DIC='324561157'
        item.medicalrecod='very sick'
        item.save()
        record=DoctorModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_patient2(self):
        item=PatientModel()
        item.ID='324561256'
        item.firstname='Matan'
        item.lastname='Sasi'
        item.password='1234567890'
        item.messagesent='hello world'
        item.DIC='324561257'
        item.medicalrecod='very ill'
        item.save()
        record=DoctorModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_patient3(self):
        item=PatientModel()
        item.ID='324561356'
        item.firstname='Matan'
        item.lastname='Suisa'
        item.password='1234567890'
        item.messagesent='hello world'
        item.DIC='324561357'
        item.medicalrecod='has cancer'
        item.save()
        record=DoctorModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

class message_test(TestCase):
    def test_message1(self):
        item=MessageModel()
        item.ID='322451738'
        item.messagesent='hello world'
        item.save()
        record=DoctorModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_message2(self):
        item=MessageModel()
        item.ID='322451748'
        item.messagesent='hello israel'
        item.save()
        record=DoctorModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_message3(self):
        item=MessageModel()
        item.ID='322451758'
        item.messagesent='hello taiwan'
        item.save()
        record=DoctorModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)
''''

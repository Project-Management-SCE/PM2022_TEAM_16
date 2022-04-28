from unicodedata import name
from django.test import TestCase
from django.urls import resolve, reverse
from projectapp.views import *
from projectapp.models import *
import unittest

class TestUrls(unittest.TestCase):
    def test_list_url_is_resolved(self):
        url=reverse('index')
        print(resolve(url))


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
        item.workdays='Monday'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.speciality='cancer'
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
        item.workdays='Monday'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.speciality='cancer'
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
        item.workdays='Monday'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.speciality='cancer'
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
        item.doctoranswer='hello you too'
        item.DID='324561157'
        item.medicalrecord='very sick'
        item.privaterecord='bee allergie'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.age=23
        item.poids=25
        item.taille=30
        item.allergies='bee'
        item.BMI=65
        item.phone='0521234567'
        item.medrecom='get away of bees'
        item.appointement='tuesday'
        item.save()
        record=PatientModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_patient2(self):
        item=PatientModel()
        item.ID='324561256'
        item.firstname='Matan'
        item.lastname='Sasi'
        item.password='1234567890'
        item.messagesent='hello world'
        item.doctoranswer='hello you too'
        item.DID='324561257'
        item.medicalrecord='very ill'
        item.privaterecord='bee allergie'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.age=23
        item.poids=25
        item.taille=30
        item.allergies='bee'
        item.BMI=65
        item.phone='0521234567'
        item.medrecom='get away of bees'
        item.appointement='tuesday'
        item.save()
        record=PatientModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_patient3(self):
        item=PatientModel()
        item.ID='324561356'
        item.firstname='Matan'
        item.lastname='Suisa'
        item.password='1234567890'
        item.messagesent='hello world'
        item.doctoranswer='hello you too'
        item.DID='324561357'
        item.medicalrecord='has cancer'
        item.privaterecord='bee allergie'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.age=23
        item.poids=25
        item.taille=30
        item.allergies='bee'
        item.BMI=65
        item.phone='0521234567'
        item.medrecom='get away of bees'
        item.appointement='tuesday'
        item.save()
        record=PatientModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

class message_test(TestCase):
    def test_message1(self):
        item=MessageModel()
        item.ID='322451738'
        item.message='hello world'
        item.save()
        record=MessageModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_message2(self):
        item=MessageModel()
        item.ID='322451748'
        item.message='hello israel'
        item.save()
        record=MessageModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_message3(self):
        item=MessageModel()
        item.ID='322451758'
        item.message='hello taiwan'
        item.save()
        record=MessageModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

class meds_test(TestCase):
    def test_meds1(self):
        item=MedsModel()
        item.ID=123456789
        item.name='concerta'
        item.description='focus drug'
        item.price='120'
        item.reason='no focus'
        item.type='narcoliptic'
        item.estock=25
        item.pstock=20
        item.save()
        record=MedsModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)
    
    def test_meds2(self):
        item=MedsModel()
        item.ID=123456880
        item.name='ritalin'
        item.description='focus drug'
        item.price='200'
        item.reason='no focus'
        item.type='narcoliptic'
        item.estock=35
        item.pstock=30
        item.save()
        record=MedsModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_meds3(self):
        item=MedsModel()
        item.ID=123456881
        item.name='acamol'
        item.description='anti cold'
        item.price='60'
        item.reason='has cold'
        item.type='anti cold'
        item.estock=200
        item.pstock=205
        item.save()
        record=MedsModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

class cart_test(TestCase):
    def test_cart1(self):
        item=cartModel()
        item.CID='324561156'
        item.MIDS='123456789'
        item.totalprice=205
        item.name='Matan'
        item.save()
        record=cartModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)
    
    def test_cart2(self):
        item=cartModel()
        item.CID='324561256'
        item.MIDS='123456880'
        item.totalprice=210
        item.name='Matan'
        item.save()
        record=cartModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)
    
    def test_cart3(self):
        item=cartModel()
        item.CID='324561356'
        item.MIDS='123456881'
        item.totalprice=213
        item.name='Matan'
        item.save()
        record=cartModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

class newcust_test(TestCase):
    def test_newcust1(self):
        item=newcustomerModel()
        item.firstname='Matan'
        item.lastname='Suisa'
        item.email='matan.sui1@gmail.com'
        item.phone='0521234567'
        item.save()
        record=newcustomerModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_newcust2(self):
        item=newcustomerModel()
        item.firstname='Matan'
        item.lastname='Shlomo'
        item.email='matan.shl1@gmail.com'
        item.phone='0521234467'
        item.save()
        record=newcustomerModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

    def test_newcust3(self):
        item=newcustomerModel()
        item.firstname='Matan'
        item.lastname='Gershon'
        item.email='matan.gersh1@gmail.com'
        item.phone='0521334567'
        item.save()
        record=newcustomerModel.objects.get()
        print("WORKS")
        self.assertEqual(record,item)

        


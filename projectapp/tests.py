from unicodedata import name
from django.test import TestCase
from django.urls import resolve, reverse
from projectapp.views import *
from projectapp.models import Adminmodel
import unittest

from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from django.contrib.auth.models import User
from chromedriver_py import binary_path

# from integration_tests.testing_tools import SeleniumTestCase
import time




class TestUrls(unittest.TestCase):
    def test_list_url_is_resolved(self):
        url=reverse('index')
        print(resolve(url))

class SeleniumTestCase(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        #service = Service(f"{settings.BASE_DIR}/chromedriver")
        service = Service(binary_path)
        ###
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
# from django.core import reverse 



class AuthenticationFormTest(SeleniumTestCase):
    def test_authentication_form(self):
        # Create a user to login with
        user = User.objects.create_user(
            username="test@user.com", password="12345"
        )

        # Go to the login page
        
        #self.driver.get("http://8000/projectapp/userlogin")
        self.driver.get(self.live_server_url + "/customers/loginpage/")

        # Find HTML elements
        username_input = self.driver.find_element_by_name("ID")
        password_input = self.driver.find_element_by_name("password")
        login_button = self.driver.find_elements_by_name("but_sub")
        
        username_input.send_keys("test@user.com")
        password_input.send_keys("12345")
        login_button.click()

        # Wait for request
        time.sleep(0.5)

        # Check that the user is logged in
        self.assertEqual(self.driver.current_url, self.live_server_url + "/userdash/")

# client = Client()
# class MainTest(TestCase):
# #     ##user login in django
# #    def user_login(self, username, password):
# #         response = self.client.login(username=username, password=username)
# #         return self.assertEqual(response.status_code, 200)
#    ## first case
#    def detail(self):
#      response = self.client.get('/testcam/<test_num>/') ## url regex
#      self.assertEquals(response.status_code, 200)

#    def detail2(self):
#        response = self.client.get(reverse('userlogin'))
#        self.assertEqual(response.status_code, 200)

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
        self.assertEqual(record,item)

class message_test(TestCase):
    def test_message1(self):
        item=MessageModel()
        item.ID='322451738'
        item.message='hello world'
        item.save()
        record=MessageModel.objects.get()
        self.assertEqual(record,item)

    def test_message2(self):
        item=MessageModel()
        item.ID='322451748'
        item.message='hello israel'
        item.save()
        record=MessageModel.objects.get()
        self.assertEqual(record,item)

    def test_message3(self):
        item=MessageModel()
        item.ID='322451758'
        item.message='hello taiwan'
        item.save()
        record=MessageModel.objects.get()
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
        self.assertEqual(record,item)
    
    def test_cart2(self):
        item=cartModel()
        item.CID='324561256'
        item.MIDS='123456880'
        item.totalprice=210
        item.name='Matan'
        item.save()
        record=cartModel.objects.get()
        self.assertEqual(record,item)
    
    def test_cart3(self):
        item=cartModel()
        item.CID='324561356'
        item.MIDS='123456881'
        item.totalprice=213
        item.name='Matan'
        item.save()
        record=cartModel.objects.get()
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
        self.assertEqual(record,item)

    def test_newcust2(self):
        item=newcustomerModel()
        item.firstname='Matan'
        item.lastname='Shlomo'
        item.email='matan.shl1@gmail.com'
        item.phone='0521234467'
        item.save()
        record=newcustomerModel.objects.get()
        self.assertEqual(record,item)

    def test_newcust3(self):
        item=newcustomerModel()
        item.firstname='Matan'
        item.lastname='Gershon'
        item.email='matan.gersh1@gmail.com'
        item.phone='0521334567'
        item.save()
        record=newcustomerModel.objects.get()
        self.assertEqual(record,item)

from django.contrib.auth.models import User
# from integration_tests.testing_tools import SeleniumTestCase
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class SeleniumTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        #service = Service(f"{settings.BASE_DIR}/chromedriver")
        cls.driver = webdriver.Chrome(executable_path='projectapp/chromedriver.exe', options=options)
        # cls.driver = webdriver.Remote(
        #     f"http://localhost:4444/wd/hub", options=options
        # )
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()


class AuthenticationFormTest(SeleniumTestCase):
    def test_authentication_form(self):
        # Create a user to login with
        user = User.objects.create_user(
            username="332531235", password="Aa123456"
        )
        print("usercreated")

        # Go to the login page
        self.driver.get("http://localhost:8000/projectapp/userlogin")
        print("connection to website")
        # Find HTML elements
        username_input = self.driver.find_element_by_id("Id")
        password_input = self.driver.find_element_by_id("password")
        error_message = self.driver.find_element_by_css_selector(".error")
        login_button = self.driver.find_element_by_id("but_sub")

        # Type in an email that doesn't exist
        username_input.send_keys("332531235")

        # Ensure that the submit button is disabled
        # Type in a password
        password_input.send_keys("Aa123456")
        login_button.click()

        # Wait for request
        time.sleep(0.5)

        # Check that the user is logged in
        self.assertEqual(self.driver.current_url,"http://localhost:8000/projectapp/index")

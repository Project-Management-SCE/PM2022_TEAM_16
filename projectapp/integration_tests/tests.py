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
        cls.driver = webdriver.Chrome(executable_path='KelaclinicProject\\PM2022_TEAM_16\\projectapp\\integration_tests\\chromedriver.exe', options=options)
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
            username="Uhtred770@gmail.com", email="test@user.com", password="UhtredBebbanburg"
        )

        # Go to the login page
        self.driver.get("http://127.0.0.1:8000/projectapp/userlogin")

        # Find HTML elements
        username_input = self.driver.find_element_by_id("Id")
        password_input = self.driver.find_element_by_id("password")
        error_message = self.driver.find_element_by_css_selector(".error")
        login_button = self.driver.find_element_by_id("but_sub")

        # Type in an email that doesn't exist
        username_input.send_keys("wrong@user.com")

        # Ensure that the submit button is disabled
        self.assertFalse(login_button.is_enabled())

        # Type in a password
        password_input.send_keys("wrongpassword")
        login_button.click()

        # Wait for request
        time.sleep(0.5)

        # Check that the error message is displayed
        self.assertEqual(error_message.text, "A user with this email address does not exist.")

        # Type in an email that does exist but with the wrong password
        username_input.clear()

        username_input.send_keys(user.username)
        login_button.click()

        # Wait for request
        time.sleep(0.5)

        # Check that the correct error message is displayed
        self.assertEqual(error_message.text, "You entered the wrong password.")

        # Type in the correct email and password
        password_input.clear()
        password_input.send_keys(user.password)
        login_button.click()

        # Wait for request
        time.sleep(0.5)

        # Check that the user is logged in
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/projectapp/homepage")

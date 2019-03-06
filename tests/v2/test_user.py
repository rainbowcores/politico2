import unittest
import json
import psycopg2
from instance.config import app_config
from app import create_app
from app.v2.models.database.maindb import drop_tables


class UserTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.usersignup = {
            "firstname": "Njeri",
            "lastname": "Museu",
            "nationalid": "33333333",
            "email": "mim@kkkkkk.com",
            "phone_number": "0725358918",
            "passport_url": "wwwuuuu",
            "password": "3676788"
        }
        self.usermissing = {
            "firstname": "Njeri",
            "lastname": "Museu",
            "nationalid": "23456178",
            "email": "mim@mim.com",
            "phone_number": "0725358918",
            "passport_url": "wwwuuuu"
            }
        self.loginwrongemail = {
            "email": "jmm@mim.com",
            "password": "23232323"
        }
        self.reset = {
            "email": "mim@kkkkkk.com"
        }

    def tearDown(self):
        drop_tables()

    def test_signup(self):
        request = self.client.post('/api/v2/auth/signup', json=self.usersignup)
        self.assertEqual(request.status_code, 201)
        ee = json.loads(
           request.data.decode("utf-8"))
        print(ee)

    def test_signup_missing(self):
        request = self.client.post('/api/v2/auth/signup', json=self.usermissing)
        self.assertEqual(request.status_code, 400)
    
    def test_reset_password(self):
        self.client.post('/api/v2/auth/signup', json=self.usersignup)
        request = self.client.post('/api/v2/auth/reset', json=self.reset)
        self.assertEqual(request.status_code, 200)

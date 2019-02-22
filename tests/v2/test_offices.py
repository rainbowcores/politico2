
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
        self.politicaloffice = {
            "office_type": "County",
            "name": "GovernorKiambu"
            }
        self.changepoliticaloffice = {
            "office_type": "County",
            "name": "GovernorNRB"
            }
        self.missingpoliticaloffice = {
            "name": "GovernorKiambuJI",
            }
        self.candidate = {
            "candidate": 1,
            "office": 1
        }
        self.usersignup = {
            "firstname": "Njeri",
            "lastname": "Museu",
            "nationalid": "33333333",
            "email": "mim@kkkkkk.com",
            "phone_number": "0725358918",
            "passport_url": "wwwuuuu",
            "password": "3676788"
        }

    def tearDown(self):
        drop_tables()

    def test_office_creation(self):
        response = self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.assertEqual(response.status_code, 201)

    def test_office_creation_missing_fields(self):
        response = self.client.post('/api/v2/offices', json=self.missingpoliticaloffice)
        self.assertEqual(response.status_code, 400)

    def test_creation_office_exists(self):
        self.client.post('/api/v2/offices', json=self.changepoliticaloffice)

        response = self.client.post('/api/v2/offices', json=self.changepoliticaloffice)

        self.assertEqual(response.status_code, 400)

    def test_candidate(self):
        self.client.post('/api/v2/offices', json=self.changepoliticaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        response = self.client.post('/api/v2/offices/1/register', json=self.candidate)

        self.assertEquals(response.json, dict(message='Candidate already registered', data=None, status=400))
    

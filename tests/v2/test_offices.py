
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
        self.numberofficename = {
            "office_type": "County",
            "name": 2
            }
        self.nonwordofficename = {
            "office_type": "County",
            "name": "2"
            }
        self.numberofficetype = {
            "office_type": 2,
            "name": "Governor"
            }
        self.nonwordofficetype = {
            "office_type": "2",
            "name": "Governor"
            }
        self.missingpoliticaloffice = {
            "name": "GovernorKiambuJI",
            }
        self.candidate = {
            "candidate": 1,
            "office": 1
        }
        self.missingfieldscandidate = {
            "candidate": 1
        }

        self.candidate_nooffice = {
            "candidate": 1,
            "office": 51
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
    
    def test_office_creation_number_name(self):
        response = self.client.post('/api/v2/offices', json=self.numberofficename)
        self.assertEqual(response.status_code, 400)
    
    def test_office_creation_number_name(self):
        response = self.client.post('/api/v2/offices', json=self.nonwordofficename)
        self.assertEqual(response.status_code, 400)

    def test_office_creation_number_officetype(self):
        response = self.client.post('/api/v2/offices', json=self.numberofficetype)
        self.assertEqual(response.status_code, 400)
    
    def test_office_creation_nonword_officetype(self):
        response = self.client.post('/api/v2/offices', json=self.nonwordofficetype)
        self.assertEqual(response.status_code, 400)

    def test_creation_office_exists(self):
        self.client.post('/api/v2/offices', json=self.changepoliticaloffice)

        response = self.client.post('/api/v2/offices', json=self.changepoliticaloffice)

        self.assertEqual(response.status_code, 400)

    def test_get_office(self):
        self.client.post('/api/v2/offices', json=self.changepoliticaloffice)
        response = self.client.get('/api/v2/offices/1')
        self.assertEqual(response.status_code, 200)
    
    def test_get_nooffice(self):
        self.client.post('/api/v2/offices', json=self.changepoliticaloffice)
        response = self.client.get('/api/v2/offices/44')
        self.assertEqual(response.status_code, 404)

    def test_candidate(self):
        self.client.post('/api/v2/offices', json=self.changepoliticaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        response = self.client.post('/api/v2/offices/1/register', json=self.candidate)

        self.assertEqual(response.status_code, 201)
    
    def test_candidate(self):
        self.client.post('/api/v2/offices', json=self.changepoliticaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        response = self.client.post('/api/v2/offices/1/register', json=self.missingfieldscandidate)

        self.assertEqual(response.status_code, 400)
    
    def test_candidate_exists(self):
        self.client.post('/api/v2/offices', json=self.changepoliticaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        response = self.client.post('/api/v2/offices/1/register', json=self.candidate)

        self.assertEqual(response.status_code, 400)
    
    def test_candidate_nonexistent_office(self):
        response = self.client.post('/api/v2/offices/51/register', json=self.candidate_nooffice)

        self.assertEqual(response.status_code, 404)
    
    def test_candidate_wrong_office(self):
        self.client.post('/api/v2/offices', json=self.changepoliticaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        response = self.client.post('/api/v2/offices/2/register', json=self.candidate)
        self.assertEqual(response.status_code, 400)
    

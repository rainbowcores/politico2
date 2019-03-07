import unittest
import json
import psycopg2
from instance.config import app_config
from app import create_app
from app.v2.models.database.maindb import drop_tables


class VoterTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.politicaloffice = {
            "office_type": "County",
            "name": "GovernorKiambu"
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
        self.candidate = {
            "candidate": 1,
            "office": 1
        }
        self.newvote = {
            "voter": 1,
            "candidate": 1,
            "office": 1
        }
        self.missingvote = {
            "candidate": 1,
            "office": 1
        }
        self.nonintegervoter = {
            "voter": "1",
            "candidate": 1,
            "office": 1
        }
        self.nonintegercandidate = {
            "voter": 1,
            "candidate": "1",
            "office": 1
        }
        self.nonintegeroffice = {
            "voter": 1,
            "candidate": 1,
            "office": "1"
        }
        self.voternonuser = {
            "voter": 111,
            "candidate": 1,
            "office": 1
        }
        self.candidatenotregisteredforoffice = {
            "voter": 1,
            "candidate": 1,
            "office": 12
        }

    def test_add_vote(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        response = self.client.post('/api/v2/vote', json=self.newvote)
        self.assertEqual(response.status_code, 201)
    
    def test_vote_missing_fields(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        response = self.client.post('/api/v2/vote', json=self.missingvote)
        self.assertEqual(response.status_code, 400)
    
    def test_vote_noninteger_voter(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        response = self.client.post('/api/v2/vote', json=self.nonintegervoter)
        self.assertEqual(response.status_code, 400)
    
    def test_vote_noninteger_candidate(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        response = self.client.post('/api/v2/vote', json=self.nonintegercandidate)
        self.assertEqual(response.status_code, 400)

    def test_vote_noninteger_office(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        response = self.client.post('/api/v2/vote', json=self.nonintegeroffice)
        self.assertEqual(response.status_code, 400)
    
    def test_voter_nonuser(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        response = self.client.post('/api/v2/vote', json=self.voternonuser)
        self.assertEqual(response.status_code, 404)
    
    def test_candidate_not_registered_office(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        response = self.client.post('/api/v2/vote', json=self.candidatenotregisteredforoffice)
        self.assertEqual(response.status_code, 400)

    def test_add_vote_wrong(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        self.client.post('/api/v2/vote', json=self.newvote)
        response = self.client.post('/api/v2/vote', json=self.newvote)
        self.assertEqual(response.status_code, 400)

    def test_results(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        self.client.post('/api/v2/vote', json=self.newvote)
        response = self.client.get('/api/v2/offices/1/result')
        self.assertEqual(response.status_code, 200)

    def test_results_wrongoffice(self):
        self.client.post('/api/v2/offices', json=self.politicaloffice)
        self.client.post('/api/v2/auth/register', json=self.usersignup)
        self.client.post('/api/v2/offices/1/register', json=self.candidate)
        self.client.post('/api/v2/vote', json=self.newvote)
        response = self.client.get('/api/v2/offices/100/result')
        self.assertEqual(response.status_code, 404)
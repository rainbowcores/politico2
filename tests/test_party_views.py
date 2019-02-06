import unittest
import os
import json
from app import create_app
#from app.v1.views import politicalparties

class PoliticalPartiesTestCase(unittest.TestCase):

    #This class represents the political parties test case
    
    def setUp(self):
        """ Initialize app and test variables """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.politicalparty = { 
            "name" : "African Liberation Party" ,
            "abbreviation" : "ALP" ,
            "members" : "15" ,
            "headquarters": "Biafra House, Kaaunda Road",
            "chairperson": "Betty Sade"
            }

    def test_politicalparty_creation (self):
        """Test that API can create political party"""
        response = self.client.post('/api/v1/politicalparties', json=self.politicalparty)
        self.assertEqual(response.status_code, 201)
    
    def test_view_all_parties(self):
        """Test that API can view all political parties"""
        response = self.client.get('/api/v1/politicalparties', json=self.politicalparty)

        self.assertEqual(response.status_code, 200)
    
    def test_view_specific_party(self):
        response = self.client.get('/api/v1/politicalparties/1', json=self.politicalparty)
        self.assertEqual(response.status_code, 200)
        



import unittest
import os
import json
from app import create_app

class PoliticalOfficesTestCase(unittest.TestCase):

    #This class represents the political offices test case
    
    def setUp(self):
        """ Initialize app and test variables """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.politicaloffice = { 
            "office_type" : "County" ,
            "name" : "Governor Kiambu" 
            }

    def test_politicaloffice_creation (self):
        """Test that API can create political office"""
        response = self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)
        self.assertEqual(response.status_code, 201)
    
    def test_view_all_offices(self):
        """Test that API can view all political parties"""
        response = self.client.get('/api/v1/politicaloffices', json=self.politicaloffice)

        self.assertEqual(response.status_code, 200)

    def test_view_specific_office(self):
        response = self.client.get('/api/v1/politicaloffices/1', json=self.politicaloffice)
        self.assertEqual(response.status_code, 200)

    """def test_delete_specific_office(self):
        response = self.client.get('/api/v1/politicaloffices/delete/1', json=self.politicaloffice)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/v1/politicaloffices/1')
        self.assertEqual(response.status_code, 400)"""



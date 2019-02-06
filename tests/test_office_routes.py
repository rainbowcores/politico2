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
            "type" : "County" ,
            "name" : "Governor Kiambu" 
            }

    def test_politicaloffice_creation (self):
        """Test that API can create political party"""
        response = self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)
        self.assertEqual(response.status_code, 201)

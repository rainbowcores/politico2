import os
from tests.test_base import BaseTest

class PoliticalOfficesTestCase(BaseTest):

    #This class represents the political offices test case
    
    

    def test_politicaloffice_creation (self):
        """Test that API can create political office"""
        response = self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)
        self.assertEqual(response.status_code, 201)
    
    def test_politicaloffice_empty_fields (self):
        """Test that API can create political office"""

        response = self.client.post('/api/v1/politicaloffices', json=self.missingpoliticaloffice)
        self.assertEqual(response.status_code, 400)

    def test_politicaloffice_datatype_fields (self):
        response = self.client.post('/api/v1/politicaloffices', json=self.stringpoliticaloffice)
        self.assertEqual(response.status_code, 400)
    
    def test_view_all_offices(self):
        """Test that API can view all political offices"""
        response = self.client.get('/api/v1/politicaloffices', json=self.politicaloffice)

        self.assertEqual(response.status_code, 200)

    def test_view_specific_office(self):
        self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)

        response = self.client.get('/api/v1/politicaloffices/1')
        self.assertEqual(response.status_code, 200)
    


    #def test_delete_specific_office(self):
        #response = self.client.get('/api/v1/politicaloffices/delete/1', json=self.politicaloffice)
        #self.assertEqual(response.status_code, 200)
        #response = self.client.get('/api/v1/politicaloffices/1')
        #self.assertEqual(response.status_code, 400)



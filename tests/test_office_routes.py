import os
from tests.test_base import BaseTest

class PoliticalOfficesTestCase(BaseTest):

    #This class represents the political offices test case
    
    

    def test_politicaloffice_creation (self):
        
        response = self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)
        self.assertEqual(response.status_code, 201)

    def test_office_creation_missing_fields(self):
        response = self.client.post('/api/v1/politicaloffices', json=self.missingpoliticaloffice)
        self.assertEqual(response.status_code, 400)
    
    
    def test_view_all_parties (self):
        response = self.client.get('/api/v1/politicaloffices', json=self.politicaloffice)
        self.assertEqual(response.status_code, 200)

    def test_view_specific_party(self):
        response = self.client.get('/api/v1/politicaloffices/1', json=self.politicaloffice)
        self.assertEqual(response.status_code, 200)
    
    def test_view_specific_party_absent(self):
        self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)
        response= self.client.get('/api/v1/politaloffices/14')
        self.assertEqual(response.status_code, 404)

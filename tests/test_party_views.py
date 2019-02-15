
import os
from tests.test_base import BaseTest


class PoliticalPartiesTestCase(BaseTest):

    #This class represents the political parties test case
    

    def test_politicalparty_creation (self):
        
        response = self.client.post('/api/v1/politicalparties', json=self.politicalparty)
        self.assertEqual(response.status_code, 201)

    def test_party_creation_missing_fields(self):
        response = self.client.post('/api/v1/politicalparties', json=self.missingpoliticalparty)
        self.assertEqual(response.status_code, 409)

    def test_creation_party_exists(self):
        self.client.post('/api/v1/politicalparties', json=self.politicalparty)

        response = self.client.post('/api/v1/politicalparties', json=self.politicalparty)

        self.assertEqual(response.status_code, 409)

    def test_view_all_parties(self):
        
        response = self.client.get('/api/v1/politicalparties', json=self.politicalparty)
        self.assertEqual(response.status_code, 200)
    
    def test_view_specific_party(self):
        response = self.client.get('/api/v1/politicalparties/1', json=self.politicalparty)
        self.assertEqual(response.status_code, 200)
    
    def test_view_specific_party_not_found(self):

        self.client.post('/api/v1/politicalparties', json=self.politicalparty)
        response = self.client.get('/api/v1/politicalparties/14')
        self.assertEqual(response.status_code, 404)

    def test_delete_specific_party(self):
        
        response = self.client.delete('/api/v1/politicalparties/1', json=self.politicalparty)
        self.assertEqual(response.status_code, 204)

    

    def test_delete_party_not_found(self):

        self.client.post('/api/v1/politicalparties', json=self.politicalparty)
        response = self.client.delete('/api/v1/politicalparties/14')
        self.assertEqual(response.status_code, 404)

    def test_wrong_delete_get_method_by_id(self):
        response = self.client.post('/api/v1/politicalparties/1', json=self.politicalparty)
        self.assertEqual(response.status_code, 405)

    def test_edit_specific_party(self):
        self.client.post('/api/v1/politicalparties', json=self.politicalparty)

        response = self.client.patch('/api/v1/politicalparties/1', json=self.changepoliticalparty)

        self.assertEqual(response.status_code, 200)
    
    def test_edit_party_name_exists(self):
        self.client.post('/api/v1/politicalparties', json=self.politicalparty)

        response = self.client.patch('/api/v1/politicalparties/1', json=self.politicalparty)

        self.assertEqual(response.status_code, 409)
    def test_edit_party_not_found(self):

        self.client.post('/api/v1/politicalparties', json=self.politicalparty)
        response = self.client.patch('/api/v1/politicalparties/14/Orange')
        self.assertEqual(response.status_code, 404)

    def test_wrong_edit_method_by_id(self):
        response = self.client.post('/api/v1/politicalparties/1', json=self.politicalparty)
        self.assertEqual(response.status_code, 405)
    
    


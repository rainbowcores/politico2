import os
from tests.v1.test_base import BaseTest


class PoliticalOfficesTestCase(BaseTest):

    def test_politicaloffice_creation(self):
        response = self.client.post('/api/v1/politicaloffices', json=self.newpoliticaloffice)
        self.assertEqual(response.status_code, 201)

    def test_office_creation_missing_fields(self):
        response = self.client.post('/api/v1/politicaloffices', json=self.missingpoliticaloffice)
        self.assertEqual(response.status_code, 400)

    def test_creation_office_exists(self):
        self.client.post('/api/v1/politicaloffices', json=self.changepoliticaloffice)

        response = self.client.post('/api/v1/politicaloffices', json=self.changepoliticaloffice)

        self.assertEqual(response.status_code, 409)

    def test_view_all_offices(self):
        response = self.client.get('/api/v1/politicaloffices', json=self.politicaloffice)
        self.assertEqual(response.status_code, 200)

    def test_view_specific_office(self):
        response = self.client.get('/api/v1/politicaloffices/2', json=self.newpoliticaloffice)
        self.assertEqual(response.status_code, 200)

    def test_view_specific_office_absent(self):
        self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)
        response = self.client.get('/api/v1/politaloffices/14')
        self.assertEqual(response.status_code, 404)

    def test_delete_specific_office(self):

        response = self.client.delete('/api/v1/politicaloffices/1', json=self.politicaloffice)
        self.assertEqual(response.status_code, 200)

    def test_delete_office_not_found(self):

        self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)
        response = self.client.delete('/api/v1/politicaloffices/14')
        self.assertEqual(response.status_code, 404)

    def test_edit_specific_office(self):
        self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)

        response = self.client.patch('/api/v1/politicaloffices/2', json=self.changepoliticaloffice)

        self.assertEqual(response.status_code, 200)

    def test_edit_office_name_exists(self):
        self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)

        response = self.client.patch('/api/v1/politicaloffices/3', json=self.politicaloffice)

        self.assertEqual(response.status_code, 409)

    def test_edit_office_not_found(self):

        self.client.post('/api/v1/politicaloffices', json=self.othernewpoliticaloffice)

        response = self.client.patch('/api/v1/politicaloffices/146', json=self.newerpoliticaloffice)
        self.assertEqual(response.status_code, 404)

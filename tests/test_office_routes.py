import os
from tests.test_base import BaseTest

class PoliticalOfficesTestCase(BaseTest):

    #This class represents the political offices test case
    
    

    def test_politicaloffice_creation (self):
        
        response = self.client.post('/api/v1/politicaloffices', json=self.politicaloffice)
        self.assertEqual(response.status_code, 201)
    
    



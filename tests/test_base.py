import unittest
import os
import json
from app import create_app



class BaseTest(unittest.TestCase):

    
    
    def setUp(self):
        
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.politicalparty = { 
          
            "name" : "AfricanLiberationParty" ,
            "logoUrl" : "ALP" ,
            "hqAddress" : "Biafra"
        }
        self.changepoliticalparty = { 
          
            "name" : "OrangeLiberationParty", 
            "logoUrl" : "ALP" ,
            "hqAddress" : "Biafra"
        }
        self.missingpoliticalparty = { 
          
            "name" : "NewLevelParty"
        }
        
        self.politicaloffice = { 
            "office_type" : "County" ,
            "name" : "GovernorKiambu" 
            }

        self.missingpoliticaloffice = { 
            "name" : "GovernorKiambu" 
            }
        
        

    def tearDown(self):
        self.app = None
        self.politicalparty = { }
        self.politicaloffice = { }
        
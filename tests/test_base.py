import unittest
import os
import json
from app import create_app


class BaseTest(unittest.TestCase):

    
    
    def setUp(self):
        
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.politicalparty = { 
          
            "name" : "African Liberation Party" ,
            "abbreviation" : "ALP" ,
            "members" : "15" ,
            "headquarters": "Biafra House, Kaaunda Road",
            "chairperson": "Betty Sade"
        }

        self.missingpoliticalparty = { 
          
            "name" : "African Liberation Party" ,
            "abbreviation" : "ALP" ,
            "members" : "15" ,
            "headquarters": "Biafra House, Kaaunda Road",
            }
        self.stringpoliticalparty = { 
          
            "name" : "African Liberation Party" ,
            "abbreviation" : 5 ,
            "members" : "15" ,
            "headquarters": "1",
            }
        self.memberpoliticalparty = { 
          
            "name" : "African Liberation Party" ,
            "abbreviation" : "ALP" ,
            "members" : "M5",
            "headquarters": "KAUNDA",
            }
        self.politicaloffice = { 
            "office_type" : "County" ,
            "name" : "Governor Kiambu" 
            }
        self.missingpoliticaloffice = { 
            "office_type" : "County" 
            }
        self.stringpoliticaloffice = { 
            "office_type" : 1 ,
            "name" : "Governor Kiambu" 
            }
        

    def tearDown(self):
        self.app = None
        self.politicalparty = { }
        self.politicaloffice = { }
        
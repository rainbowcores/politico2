politicalparties_list = []

class PartyModel:
    
    
    
    

    def __init__(self, name=None, logoUrl=None, hqAddress=None):
        self.name = name
        self.logoUrl = logoUrl
        self.hqAddress= hqAddress
        self.party_id= len(politicalparties_list)+1

        PartyModel.party_id= self.party_id

    def to_json(self):
   
        
        return dict(
            party_id = self.party_id,
            name = self.name ,
            logoUrl = self.logoUrl ,
            hqAddress=self.hqAddress
            

        )
    @staticmethod
    def get_specific_party(party_id):
        for party in politicalparties_list:
            if party.party_id == party_id:
               return party

    @staticmethod
    def get_specific_party_name(name):
        for party in politicalparties_list:
            if party.name == name:
               return party
    
    @staticmethod
    def patch_party_name(party_id, name=None, logoUrl=None, hqAddress=None):
        party= PartyModel.get_specific_party(party_id)
        party.name= name
        party.logoUrl= logoUrl
        party.hqAddress= hqAddress
        return party
               
    
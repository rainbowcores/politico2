politicaloffices_list = []

class OfficeModel:
    
    
    office_id= 1
    

    def __init__(self, name=None, office_type=None):
        self.name = name
        self.office_type = office_type
        
        self.office_id= len(politicaloffices_list)+1

        OfficeModel.office_id= len(politicaloffices_list)+1

    def to_json(self):
   
        
        return dict(
            office_id = self.office_id,
            name = self.name ,
            office_type = self.office_type 
            

        )
    @staticmethod
    def get_specific_office(office_id):
        for office in politicaloffices_list:
            if office.office_id == office_id:
               return office
    
    
               
    
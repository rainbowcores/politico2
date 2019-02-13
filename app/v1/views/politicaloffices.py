
from flask import Flask, make_response, jsonify, request, Blueprint
from .politicalmain import api, response
from ..models.officesmodel import OfficeModel, politicaloffices_list

app = Flask(__name__)





@api.route('/politicaloffices', methods = ["POST", "GET"])
def add_politicaloffices():
   
    #Create a new political office  - POST request
    
    if request.method == "POST":
        data = request.get_json()
        office_type = data ['office_type']
        name = data ['name']
        
        if not office_type.isalpha() or not name.isalpha():
            return response (400, "Please fill in all the fields, office type and name should be txt", [])

        else:
            new_politicaloffice= OfficeModel(name, office_type)
            politicaloffices_list.append(new_politicaloffice)
                
            return response (201, "New office was created", [new_politicaloffice.to_json()])


    elif request.method == "GET":
        #Get all political offices - GET request
        return response(200, "", [office.to_json() for office in politicaloffices_list])

@api.route('/politicaloffices/<int:office_id>', methods = ["GET"])
def specific_politicaloffice(office_id):
    #View specific political office - GET request
    global politicaloffices_list

    office= OfficeModel.get_specific_office(office_id)
    return response(200, "", [office.to_json()])


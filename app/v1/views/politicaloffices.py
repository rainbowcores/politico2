
from flask import Flask, make_response, jsonify, request, Blueprint
from .politicalmain import api, response

app = Flask(__name__)


politicaloffices_list = []



@api.route('/politicaloffices', methods = ["POST", "GET"])
def add_politicaloffices():
   
    #Create a new political office  - POST request
    
    if request.method == "POST":
        try:
            data = request.get_json()
            office_type = data ['office_type']
            name = data ['name']
            
            new_politicaloffice ={ 
                    "office_id": len(politicaloffices_list) + 1,
                
                    "office_type" : office_type ,
                    "name" : name 
                    
                    }
            if not office_type.isalpha() or not name.isalpha():
                pass
        except:
            return response (400, "Please fill in all the fields as required and as text", [])

        else:
            office_id = len(politicaloffices_list) + 1
            politicaloffices_list.append(new_politicaloffice)
                
            return response (201, "", [
                {
                    "id" : office_id,
                    "name" : name,
                }])

    elif request.method == "GET":
        #Get all political offices - GET request
        return response(200, "", politicaloffices_list)

@api.route('/politicaloffices/<int:office_id>', methods = ["GET"])
def specific_politicaloffice(office_id):
    #View specific political office - GET request
    new_politicaloffice = [new_politicaloffice for new_politicaloffice in politicaloffices_list if new_politicaloffice['office_id'] == office_id]
    return response(200, "", new_politicaloffice)



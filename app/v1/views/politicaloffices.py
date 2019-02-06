
from flask import Flask, make_response, jsonify, request, Blueprint, abort
from .politicalmain import api

app = Flask(__name__)


politicaloffices_list = []
def generate_id(list):
    """ Creates a unique ID for a new item to be added to the list"""

    return len(list) + 1

@api.route('/politicaloffices', methods = ["POST", "GET"])
def add_politicaloffices():
    """
        Create a new political office  - POST request
    """
    if request.method == "POST":
        data = request.get_json()
        office_type = data ['office_type']
        name = data ['name']
        

        new_politicaloffice = { 
                "id": generate_id(politicaloffices_list),
                "type" : office_type ,
                "name" : name 
                
                }
        
        politicaloffices_list.append(new_politicaloffice)
        
        return make_response(jsonify({
            "Message": "New Political Office Created",
            "office name": new_politicaloffice['name'],
            "office id": new_politicaloffice['id'],
            }), 201)

    elif request.method == "GET":
        #Get all political offices - GET request
        return make_response(jsonify({
                "offices": politicaloffices_list,
                "status": "Ok"
            }), 200)

@api.route('/politicaloffices/<int:id>', methods = ["GET"])
def specific_politicaloffice(id):
    #View specific political party - GET request
    new_politicaloffice = [new_politicaloffice for new_politicaloffice in politicaloffices_list if new_politicaloffice['id'] == id]
    
    if len(new_politicaloffice) == 0:
        abort(404, 'Office does not exist')

    if request.method == 'GET':
        return make_response(jsonify({
                    "parties": politicaloffices_list,
                    "status": "Ok"
                }), 200)



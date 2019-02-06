
from flask import Flask, make_response, jsonify, request, abort
from .politicalmain import api

app = Flask(__name__)


politicalparties_list = []
def generate_id(list):
    """ Creates a unique ID for a new item to be added to the list"""

    return len(list) + 1

@api.route('/politicalparties', methods = ["POST","GET"])
def add_politicalparties():
    """
        Create a new political party  - POST request
    """
    if request.method == "POST":

        data = request.get_json()
        name = data ['name']
        abbreviation = data ['abbreviation']
        members = data ['members']
        headquarters = data ['headquarters']
        chairperson = data ['chairperson']

        new_politicalparty = { 
                "id": generate_id(politicalparties_list),
                "name" : name ,
                "abbreviation" : abbreviation ,
                "members" : members ,
                "headquarters": headquarters,
                "chairperson": chairperson
                }
        
        politicalparties_list.append(new_politicalparty)
        
        return make_response(jsonify({
            "Message": "New Political Party Created",
            "party name": new_politicalparty['name'],
            "party id": new_politicalparty['id'],
         }), 201)


    elif request.method == "GET":
        return make_response(jsonify({
                "parties": politicalparties_list,
                "status": "Ok"
            }), 200)

@api.route('/politicalparties/<int:id>', methods = ["GET"])
def specific_politicalparty(id):
    #View specific political party - GET request
    new_politicalparty = [new_politicalparty for new_politicalparty in politicalparties_list if new_politicalparty['id'] == id]
    
    if len(new_politicalparty) == 0:
        abort(404, 'Party does not exist')

    if request.method == 'GET':
        return make_response(jsonify({
                    "parties": politicalparties_list,
                    "status": "Ok"
                }), 200)


            



from flask import Flask, make_response, jsonify, request
from .politicalmain import api

app = Flask(__name__)


politicalparties_list = []
def generate_id(list):
    """ Creates a unique ID for a new item to be added to the list"""

    return len(list) + 1

@api.route('/politicalparties', methods = ["POST"])
def add_politicalparties():
    """
        Create a new political party  - POST request
    """
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

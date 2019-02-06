
from flask import Flask, make_response, jsonify, request, Blueprint
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
        type = data ['type']
        name = data ['name']
        

        new_politicaloffice = { 
                "id": generate_id(politicaloffices_list),
                "type" : type ,
                "name" : name 
                
                }
        
        politicaloffices_list.append(new_politicaloffice)
        return make_response(jsonify({
            "Message": "New Political Office Created",
            "office name": new_politicaloffice['name'],
            "office id": new_politicaloffice['id'],
    }), 201)

    elif request.methods == "GET":
        return make_response(jsonify(politicaloffices_list), 200)



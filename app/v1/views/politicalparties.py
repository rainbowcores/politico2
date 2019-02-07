
from flask import Flask, make_response, jsonify, request, abort
from .politicalmain import api, response

app = Flask(__name__)


politicalparties_list = []
party_id = len(politicalparties_list) + 1


@api.route('/politicalparties', methods = ["POST","GET"])
def add_politicalparties():
    #Create a new political party  - POST request
    
    if request.method == "POST":
        try: 

            data = request.get_json()
            
            name = data['name']
            abbreviation = data['abbreviation']
            members = data['members']
            headquarters = data['headquarters']
            chairperson = data['chairperson']

            new_politicalparty = { 
                    "party_id": party_id,
                    "name" : name ,
                    "abbreviation" : abbreviation ,
                    "members" : members ,
                    "headquarters": headquarters,
                    "chairperson": chairperson
                    }
            if not name.isalpha() or not abbreviation.isalpha() or not headquarters.isalpha() or not chairperson.isalpha():
                pass
            if not members.isdigit():
                pass
            
            

        except:
                return response (400, "Please fill in all the fields as required: members as numbers, the rest as text",[])

        else:

            politicalparties_list.append(new_politicalparty)
        
            return response (201, "", [
                    {
                        "id" : party_id,
                        "name" : name,
                    }])


    elif request.method == "GET":
    
        return response(200, "", politicalparties_list)

@api.route('/politicalparties/<int:party_id>', methods = ["GET", "DELETE"])
def specific_politicalparty(party_id):
    #View specific political party - GET request
    new_politicalparty = [new_politicalparty for new_politicalparty in politicalparties_list if new_politicalparty['party_id'] == party_id]
    
    if len(new_politicalparty) == 0:
        return response(404, "party does not exist", [])

    else:
        if request.method == 'GET':
            return response(200, "", new_politicalparty)
        
        elif request.method == 'DELETE':
            
            new_politicalparty.pop

            return response(204, "Party with id {} deleted".format(party_id), [] )
        
        else:

            return response(405, "The method used is not allowed", [])



@api.route('/politicalparties/<int:party_id>/<string:name>', methods = ["PATCH"])
def edit_party_name(party_id, name):

    new_politicalparty = [new_politicalparty for new_politicalparty in politicalparties_list if new_politicalparty['party_id'] == party_id]
    
    if len(new_politicalparty) == 0:
        return response(404, "party does not exist", [])

    elif request.method != 'PATCH':

            return response(405, "The method used is not allowed", [])
    
    else:
        for i in range(len(politicalparties_list)):
            if politicalparties_list[i]['party_id'] == party_id:
                politicalparty = politicalparties_list[i]
                politicalparty['name'] = name
                politicalparties_list[i] = politicalparty
                
        
        return response (200, "", [
                    {
                        "id" : party_id,
                        "name" : name,
                    }])

from flask import Flask, make_response, jsonify, request, Blueprint, json
from .politicalmain import api, response
from . .models.partiesmodel import PartyModel, politicalparties_list
app = Flask(__name__)







@api.route('/politicalparties', methods = ["POST","GET"])
def add_politicalparties():
    #Create a new political party  - POST request
    
    if request.method == "POST":
        data = request.get_json()
        name = data['name']
        logoUrl = data['logoUrl']
        hqAddress = data['hqAddress']

        if not name.isalpha() or not logoUrl.isalpha() or not hqAddress.isalpha():
            return response (400, "Please fill in all the fields as required: members as numbers, the rest as text",[])
       
        else:

            new_politicalparty= PartyModel(name, logoUrl, hqAddress)
            
            politicalparties_list.append(new_politicalparty)
            
            return response (201, "New party was created", [new_politicalparty.to_json()])
            

    elif request.method == "GET":
    
        return response(200, "", [party.to_json() for party in politicalparties_list])
    else:

        return response(405, "The method used is not allowed", [])

@api.route('/politicalparties/<int:party_id>', methods = ["GET", "DELETE"])
def specific_politicalparty(party_id):
    #View specific political party - GET request
    global politicalparties_list
    #new_politicalparty = [new_politicalparty for new_politicalparty in politicalparties_list if new_politicalparty['party_id'] == party_id]
    

    if request.method == "GET":
        party= PartyModel.get_specific_party(party_id)
        if party:
            return response(200, "", [party.to_json()])
        else:
            return response(404, "party does not exist", []) 
        
    elif request.method== "DELETE":
        party= PartyModel.get_specific_party(party_id) 
        if party:
            politicalparties_list.remove(party)             
            return response(204, "deleted successfully", [party.to_json() for party in politicalparties_list] )

            
        else:
            return response(404, "party does not exist", [])   
    



@api.route('/politicalparties/<int:party_id>', methods = ["PATCH"])
def edit_party_name(party_id):

    #new_politicalparty = [new_politicalparty for new_politicalparty in politicalparties_list if new_politicalparty['party_id'] == party_id]
    
    #if len(new_politicalparty) == 0:
        #return response(404, "party does not exist", [])

   
        data = request.get_json()
        name = data['name']
    
        party = PartyModel.patch_party_name(party_id, name)

        if party:
            politicalparties_list.append(party)
            return response (200, "party name changes", [party.to_json()])
        else:
            return response(404, "party does not exist", [])

from flask import Flask, make_response, jsonify, request, Blueprint, json
from .politicalmain import api, response
from ..models.partiesmodel import PartyModel, politicalparties_list
app = Flask(__name__)







@api.route('/politicalparties', methods = ["POST","GET"])
def add_politicalparties():
    #Create a new political party  - POST request
    
    if request.method == "POST":
        data = request.get_json()
        party= PartyModel.get_specific_party_name(data['name']) 
        if not party:
            try:
                name = data['name']
                logoUrl = data['logoUrl']
                hqAddress = data['hqAddress']
                if not name.isalpha() or not logoUrl.isalpha() or not hqAddress.isalpha():
                    return response (400, "Please fill in all the fields as name, logoUrl and hqAddress as text",[])
                else:

                    new_politicalparty= PartyModel(name, logoUrl, hqAddress)
                
                    politicalparties_list.append(new_politicalparty)
                    
                    return response (201, "New party was created", [new_politicalparty.to_json()])
            except KeyError:
                return response (409, "Key error occured, please enter all the fields", [])
        else:
            return response(409, "The party exists", [])
    elif request.method == "GET":
    
        return response(200, "", [party.to_json() for party in politicalparties_list])
    else:

        return response(405, "The method used is not allowed", [])

@api.route('/politicalparties/<int:party_id>', methods = ["GET", "DELETE"])
def specific_politicalparty(party_id):
    #View specific political party - GET request
    global politicalparties_list
    

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
        data = request.get_json()
        party= PartyModel.get_specific_party_name(data['name']) 
        if not party:
            try:
                name = data['name']
                logoUrl = data['logoUrl']
                hqAddress = data['hqAddress']

                party = PartyModel.patch_party_name(party_id, name,logoUrl, hqAddress)
                if party:
                    party.name= name
                    party.logoUrl= logoUrl
                    party.hqAddress= hqAddress
                    return response (200, "party name changes", [party.to_json()])
                else:
                    return response(404, "party does not exist", [])
            except KeyError:
                return response (202, "Key error occured, please enter all the fields", [])
        else:
            return response(409, "The party name exists", [])
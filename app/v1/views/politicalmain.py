from flask import Blueprint, make_response, jsonify
api = Blueprint('api', __name__, url_prefix='/api/v1')


    #Adds a unique id to each item added to the list

    

def response(code, message, data=None):
    """ Creates a basic reposnse """
    response = {
        "status": code,
        "message": message,
        "data": data
    }
    return make_response(jsonify(response), code)




#def id_not_found (list):
    #new_politicalparty = [new_politicalparty for new_politicalparty in list if new_politicalparty['id'] == id]
    
    #if len(new_politicalparty) == 0:
        #return response(404, "party does not exist", [])

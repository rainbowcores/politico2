
from flask import Flask, make_response, jsonify, request, Blueprint, abort
from app.v2.views.mainview import thisapi, response
from app.v2.models.candidatemodel import Candidates
from app.v2.models import modeloffices
import psycopg2
from app.v2 import validations
from app.v2 import modelfunctions
from app.v2.modelfunctions import Usermethods, Officemethods, Candidatemethods


app = Flask(__name__)


@thisapi.route('/offices', methods=['POST'])
def add_politicaloffices():
    office_data = request.get_json()
    try:
        name = office_data['name']
        office_type = office_data['office_type']
    except Exception:
        return abort(response(400, "Please enter all the fields"))
    if(validations.is_string(name) is False):
        return response(400, "Name should be a string")
    if(validations.is_string(office_type) is False):
        return response(400, "Office type should be a string")
    if(validations.is_alphabetic(name) is False):
        return abort(response(400, "The name should be a word"))
    if(validations.is_alphabetic(office_type) is False):
        return abort(response(400, "The office type should be a word"))
    office = Officemethods().get_by_name(name)
    if office:
        return abort (response(400, "Office exists"))
    new_politicaloffice = modeloffices.Offices(name=name, office_type=office_type)
    office_data = new_politicaloffice.create_office()
    print(office_data)
    return response(201, "New office was created", {
        "office": {
            "name": new_politicaloffice.name,
            "office_type": new_politicaloffice.office_type,
            }
        })

@thisapi.route('/offices/<int:office_id>', methods=["GET"])
def specific_politicaloffice(office_id):
        office = Officemethods().get_by_id(office_id)
        if office:
                return response(200, "Office", office)
        else:
            return response(404, "office does not exist")

@thisapi.route('/offices/<int:office_id>/register', methods=['POST'])
def register_candidate(office_id):
    candidate_data = request.get_json()
    try:
        office = candidate_data["office"]
        candidate = candidate_data["candidate"]

    except:
        return abort(response(400, "Please enter all the fields"))
    if(validations.is_integer(candidate) is False):
        return response(400, "User should be an integer")
    if(validations.is_integer(office) is False):
        return response(400, "Office should be an integer")
    if office_id != office:
        return abort(response(400, "Please register candidate for this office only"))
    thecandidate = Usermethods().get_by_id(candidate)
    if not thecandidate:
        return response(404, "user does not exist")
    thiscandidate = Candidatemethods().candidate_registered(candidate, office)
    if thiscandidate:
        return abort(response(400, "Candidate already registered"))
    new_office = Officemethods().get_by_id(office)
    if not new_office:
        return response(404, "office does not exist")
    new_candidate = Candidates(candidate=candidate, office=office)
    data = new_candidate.create_candidate()
    print(data)
    return response(201, "candidate registered", {
        "candidate": {
            "office": new_candidate.office,
            "user": new_candidate.candidate}
        })

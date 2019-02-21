
from flask import Flask, make_response, jsonify, request, Blueprint, abort
from app.v2.views.mainview import thisapi, response
from app.v2.models.candidatemodel import Candidates
from app.v2.models.modeloffice import Offices



app = Flask(__name__)


@thisapi.route('/offices', methods=['POST'])
def add_politicaloffices(name, office_type):
    office_data = request.get_json()
    try:
        name = office_data['name']
        office_type = office_data['office_type']
    except Exception:
        return abort(response(400, "Please enter all the fields"))

    new_politicaloffice = Offices(name=name, office_type=office_type)
    office_data = new_politicaloffice.create_office()
    print(office_data)
    return response(201, "New office was created")

@thisapi.route('/offices/<int:office_id>', methods=["GET"])
def specific_politicaloffice(office_id):
        office = Offices.get_by_id(office_id)
        if office:
                return response(200, "")
        else:
            return response(404, "office does not exist")

@thisapi.route('/offices/<int:office_id>/register', methods=['POST'])
def register_candidate():
    candidate_data = request.get_json()
    try:
        office = candidate_data["office"]
        candidate = candidate_data["candidate"]
        mycandidate = Candidates.is_candidate_registered(office, candidate)
        if mycandidate:
            return abort(response(400, "User is already a candidate"))

    except Exception:
        return abort(response(400, "Please enter all the fields"))
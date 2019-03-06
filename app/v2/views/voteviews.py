from flask import Flask, make_response, jsonify, request, Blueprint, abort
from app.v2.views.mainview import thisapi, response
from app.v2.models.candidatemodel import Candidates
from app.v2.models.votesmodel import Votes
from app.v2.models import modeloffices
import psycopg2
from app.v2 import validations, modelfunctions
from app.v2.modelfunctions import Usermethods, Officemethods, Candidatemethods, Votesmethods


app = Flask(__name__)


@thisapi.route('/vote', methods=['POST'])
def vote():
    vote_data = request.get_json()
    try:
        voter = vote_data["voter"]
        office = vote_data["office"]
        candidate = vote_data["candidate"]

    except:
        return abort(response(400, "Please enter all the fields"))
    if(validations.is_integer(voter) is False):
        return response(400, "Voter should be an integer")
    if(validations.is_integer(candidate) is False):
        return response(400, "User should be an integer")
    if(validations.is_integer(office) is False):
        return response(400, "Office should be an integer")
    thevoter = Usermethods().get_by_id(voter)
    if not thevoter:
        return response(404, "Voter does not exist")
    thatcandidate = Candidatemethods().candidate_registered(candidate, office)
    if not thatcandidate:
        return abort(response(400, "Candidate is not registered for this office"))
    thatcandidate = Votesmethods().vote_exists(voter, candidate, office)
    if thatcandidate:
        return abort(response(400, "You can only vote once"))
    new_vote = Votes(voter=voter, candidate=candidate, office=office)
    data = new_vote.create_vote()
    print(data)
    return response(201, "Vote added", {
        "vote": {
            "voter": new_vote.voter,
            "office": new_vote.office,
            "candidate": new_vote.candidate}
        })

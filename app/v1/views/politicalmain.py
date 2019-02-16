from flask import Blueprint, make_response, jsonify
api = Blueprint('api', __name__, url_prefix='/api/v1')


def response(code, message, data=None):
    """ Creates a basic reposnse """
    response = {
        "status": code,
        "message": message,
        "data": data
    }
    return make_response(jsonify(response), code)

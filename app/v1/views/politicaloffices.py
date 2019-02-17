
from flask import Flask, make_response, jsonify, request, Blueprint
from .politicalmain import api, response
from ..models.officesmodel import OfficeModel, politicaloffices_list

app = Flask(__name__)


@api.route('/politicaloffices', methods=["POST", "GET"])
def add_politicaloffices():
    if request.method == "POST":
        data = request.get_json()
        try:
            name = data['name']
            office_type = data['office_type']
            if not office_type.isalpha() or not name.isalpha():
                return response(400, "Office type and name should be text", [])

            office = OfficeModel.get_specific_office_name(data['name'])
            if not office:
                new_politicaloffice = OfficeModel(name, office_type)
                politicaloffices_list.append(new_politicaloffice)
                return response(201, "New office was created", [new_politicaloffice.to_json()])
            else:
                return response(409, "The office exists", [])
        except:
            return response(409, "Please fill in all the fields, office type and name ", [])

    elif request.method == "GET":
        return response(200, "", [office.to_json() for office in politicaloffices_list])


@api.route('/politicaloffices/<int:office_id>', methods=["GET", "DELETE"])
def specific_politicaloffice(office_id):
    global politicaloffices_list
    if request.method == "GET":
        office = OfficeModel.get_specific_office(office_id)
        if office:
                return response(200, "", [office.to_json()])
        else:
            return response(404, "office does not exist", [])
    elif request.method == "DELETE":
        office = OfficeModel.get_specific_office(office_id)
        if office:
            politicaloffices_list.remove(office)
            return response(200, "deleted successfully", [office.to_json() for office in politicaloffices_list])
        else:
            return response(404, "office does not exist", [])


@api.route('/politicaloffices/<int:office_id>', methods=["PATCH"])
def edit_office(office_id):
        data = request.get_json()
        try:
            name = data['name']
            office_type = data['office_type']
            if not office_type.isalpha() or not name.isalpha():
                return response(400, "Office type and name should be text", [])

            office = OfficeModel.patch_office_name(office_id, name, office_type)
            if office:
                office.name = name
                office.office_type = office_type
                return response(200, "office details changed", [office.to_json()])
            else:
                return response(404, "office does not exist", [])
        except:
            return response(404, "error updating the office", [])
       
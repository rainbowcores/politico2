from flask import Flask, make_response, jsonify, request, Blueprint, json, abort
from app.v2.views.mainview import thisapi, response
from app.v2.models.usersmodel import Users
import os
import jwt
from app.v2 import validations
from app.v2 import modelfunctions
from app.v2.modelfunctions import Usermethods, Officemethods
import psycopg2


KEY = os.getenv('SECRET')

app = Flask(__name__)


@thisapi.route('/auth/signup', methods=['POST'])
def user_signup():
    user_data = request.get_json()
    try:
        firstname = user_data["firstname"]
        lastname = user_data["lastname"]
        nationalid = user_data["nationalid"]
        email = user_data["email"]
        phone_number = user_data["phone_number"]
        passport_url = user_data["passport_url"]
        password = user_data["password"]
    except:
        return abort(response(400, "Please enter all the fields"))
    if(validations.is_string(firstname) is False):
        return response(400, "Firstname should be a string")
    if(validations.is_string(lastname) is False):
        return response(400, "Lastname should be a string")
    if(validations.is_string(nationalid) is False):
        return response(400, "Nationalid should be a string")
    if(validations.is_string(email) is False):
        return response(400, "Email hould be a string")
    if(validations.is_string(phone_number) is False):
        return response(400, "Phonenumber should be a string")
    if(validations.is_string(passport_url) is False):
        return response(400, "Passporturl should be a string")
    if(validations.is_string(password) is False):
        return response(400, "Password should be a string")
    if (validations.spaces(user_data, ["firstname", "lastname", "username", "nationalid", "email", "phone_number", "passportUrl", "password"]) is False):
        return abort(response(400, "No field can be empty"))
    if(validations.email_type(email) is False):
        return abort(response(400, "Use a valid email"))
    if(validations.is_alphabetic(firstname) is False):
        return abort(response(400, "The first name should be a word"))
    if(validations.is_alphabetic(lastname) is False):
        return abort(response(400, "The last name should be a word"))
    if(validations.is_numbers(nationalid) is False):
        return abort(response(400, "The other name should contain character of words"))
    if(validations.validate_password(password) is False):
        return abort(response(400, "Password should be more than 6 characters with letters numbers and symbols"))
    if(validations.is_numbers(phone_number) is False):
        return abort(response(400, "Enter a correct phone number"))
    
    user = Usermethods().get_by_email(email)
    if user:
        return abort (response(400, "user exists"))
    new_user = Users(firstname=firstname, lastname=lastname, nationalid=nationalid, email=email, phone_number=phone_number, passport_url=passport_url, password=password)
    data = new_user.create_user()
    print(data)
    return response(201, "user added", {
        "user": {
            "email": new_user.email,
            "firstname": new_user.firstname}
        })
    

@thisapi.route('/auth/login', methods=['POST'])
def userlogin():
    user_login = request.get_json()
    try:
        email = user_login["email"]
        password = user_login["password"]
    except:
        return abort(response(400, "Please email and password fields"))
    if(validations.email_type(email) is False):
        return response(400, "Use a valid email")
    if(validations.is_string(password) is False):
        return response(400, "Password should be a string")
    if(validations.is_string(email) is False):
        return response(400, "Email should be a string")
    if (validations.spaces(user_login, ["email", "password"]) is False):
        return response(400, "No field can be empty")
    try:
        user = get_by_email(email)
        if not user:
            return abort(response(401, "User does not exist"))
        encoded = jwt.encode({"email": email}, KEY, algorithm='HS256')
        return response(200, "data", {
            "message": "Logged in successfully",
            "token": encoded.decode('UTF-8'),
            "user": {
                "email": email
            }
        })
    except Exception as error:
        return error
    
@thisapi.route("/auth/reset", methods=["POST"])
def reset_password():
    try:
        data = request.get_json()
        email = data["email"]
    except:
        return abort (response(400, "enter email"))

    try:
        user = get_by_email(email)
        if not user:
            return abort(response(404, "Email does not belong to any account"))
        return response(200, "Reset link sent")
    except:
        return abort(response(400, "Error sending password reset link"))

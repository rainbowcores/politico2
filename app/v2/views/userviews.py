from flask import Flask, make_response, jsonify, request, Blueprint, json, abort
from app.v2.views.mainview import thisapi, response
from app.v2.models.usersmodel import Users
import os
import jwt

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
    except Exception:
        return abort(response(400, "Please enter all the fields"))

    new_user = Users(firstname=firstname, lastname=lastname, nationalid=nationalid, email=email, phone_number=phone_number, passport_url=passport_url, password=password)
    data = new_user.create_user()
    print(data)
    return response(201, "user added")

@thisapi.route('/auth/login', methods=['POST'])
def userlogin():
    user_login = request.get_json()
    try:
        email = user_login["email"]
        password = user_login["password"]
    except:
        return abort(response(400, "Please email and password fields"))
    try:
        user = Users.get_by_email(email)
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
        user = Users.get_by_email(email)
        if not user:
            return abort(response(404, "Email does not belong to any account"))
        return response(200, "Reset link sent")
    except:
        return abort(response(400, "Error sending password reset link"))


import psycopg2
from app.v2.models.database.database_config import fetch_single_row
from app.v2.views.mainview import response
from flask import abort
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash



class Users:

    def __init__(self, firstname, lastname, nationalid, email, phone_number, passport_url, password):
        self.firstname = firstname
        self.lastname = lastname
        self.nationalid = nationalid
        self.email = email
        self.phone_number = phone_number
        self.passport_url = passport_url
        self.password = password

    def create_user(self):
        query = """ INSERT INTO users(firstname, lastname, nationalid, email, phone_number, passport_url, password) VALUES ('{}','{}', '{}', '{}', '{}', '{}', '{}')""".format(self.firstname, self.lastname, self.nationalid, self.email, self.phone_number, self.passport_url, self.password)
        user_exists = Users.get_by_email(self.email)
        print(user_exists)
        if user_exists:
            return abort(response(400, "User exists"))
        try:
            db_url = app.config["DATABASE_URL"]
            conn = psycopg2.connect(db_url)
            cur = conn.cursor()
            cur.execute(query)
            cur.close()
            conn.commit()
            conn.close()

        except Exception as error:
            return error

    def to_json(self):
        return dict(
            firstname=self.firstname,
            lastname=self.lastname,
            nationalid=self.nationalid,
            email=self.email,
            phone_number=self.phone_number,
            passport_url=self.passport_url,
            password=self.password
            )

    @staticmethod
    def get_by_email(email):
        query = """SELECT firstname, lastname, nationalid, email, phone_number, passport_url, password FROM users WHERE email='{email}';""".format(email=email)
        try:
            db_url = app.config["DATABASE_URL"]
            conn = psycopg2.connect(db_url)
            cur = conn.cursor()
            cur.execute(query)
            row = cur.fetchone()
            conn.commit()
            return row
        except Exception as error:
            return error

    

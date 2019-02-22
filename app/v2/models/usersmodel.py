import psycopg2
from app.v2.views.mainview import response
from flask import abort
from flask import current_app as app

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

    

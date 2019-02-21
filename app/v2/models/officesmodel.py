import psycopg2
from app.v2.models.database.database_config import fetch_single_row
from app.v2.views.mainview import response
from flask import abort
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash


class Offices:

    def __init__(self, name=None, office_type=None):
        self.name = name
        self.office_type = office_type

    def to_json(self):
        return dict(
            name=self.name,
            office_type=self.office_type
            )

    def create_office(self):
        query = """ INSERT INTO offices(name, office_type) VALUES ('{}','{}')""".format(self.name, self.office_type)
        office_exists = Users.get_by_email(self.name)
        if office_exists:
            return abort(response(400, "Office exists"))
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

    @staticmethod
    def get_by_id(id):
        query = """SELECT name, office_type FROM offices WHERE id='{id}';""".format(id=id)
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

    @staticmethod
    def get_by_name:
        query = """SELECT name, office_type FROM users WHERE name='{name}';""".format(name=name)
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


from app.v2.models.usersmodel import Users
from flask import abort
from app.v2.models.officesmodel import Offices
from app.v2.views.mainview import response
from flask import current_app as app
import psycopg2


class Candidates:

    def __init__(self, office, candidate):
        self.office = office
        self.candidate = candidate

    
    @staticmethod
    def create_candidate(candidate, office):
        query = """ INSERT INTO candidates('office', 'candidate') VALUES ('{}','{}')""".format(self.office, self.candidate)
        candidate_exists = Users.get_by_id(candidate)
        office_exists = Offices.get_by_id(office)
        if not candidate_exists or not office_exists:
            return abort(response(400, "Missing"))
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
            office=self.office,
            candidate=self.candidate
            )

    @staticmethod
    def is_candidate_registered(office, candidate):
        query = """SELECT office, candidate FROM candidates WHERE candidate='{candidate}' AND user='{user}' ;""".format(candidate, user)
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

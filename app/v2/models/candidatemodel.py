from app.v2.models.usersmodel import Users
from flask import abort
from app.v2.models.modeloffices import Offices
from app.v2.views.mainview import response
from flask import current_app as app
import psycopg2


class Candidates:

    def __init__(self, office, candidate):
        self.office = office
        self.candidate = candidate

    def create_candidate(self):
        query = """ INSERT INTO candidates(office, candidate) VALUES ('{}','{}')""".format(self.office, self.candidate)
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

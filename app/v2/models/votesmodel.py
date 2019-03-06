from app.v2.models.usersmodel import Users
from flask import abort
from app.v2.models.modeloffices import Offices
from app.v2.views.mainview import response
from flask import current_app as app
import psycopg2


class Votes:

    def __init__(self, voter, office, candidate):
        self.voter = voter
        self.office = office
        self.candidate = candidate

    def create_vote(self):
        query = """ INSERT INTO votes(voter, office, candidate) VALUES ('{}','{}','{}')""".format(self.voter, self.office, self.candidate)
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
            voter=self.voter,
            office=self.office,
            candidate=self.candidate
            )

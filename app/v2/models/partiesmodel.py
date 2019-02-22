import psycopg2
from app.v2.views.mainview import response
from flask import abort
from flask import current_app as app


class Offices:

    def __init__(self, name=None, logoUrl=None, hqAddress=None):
        self.name = name
        self.logoUrl = logoUrl
        self.hqAddress = hqAddress

    def to_json(self):
        return dict(
            name=self.name,
            office_type=self.office_type
            )

    def create_office(self):
        query = """ INSERT INTO parties(name=None, logoUrl=None, hqAddress=None) VALUES ('{}','{}','{}')""".format(self.name, self.logoUrl, self.hqAddress)
    
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

    

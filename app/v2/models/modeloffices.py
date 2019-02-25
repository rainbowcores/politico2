import psycopg2
from app.v2.views.mainview import response
from flask import abort
from flask import current_app as app


class Offices:

    def __init__(self, name, office_type):
        self.name = name
        self.office_type = office_type

    def to_json(self):
        return dict(
            name=self.name,
            office_type=self.office_type
            )

    def create_office(self):
        query = """ INSERT INTO offices(name, office_type) VALUES ('{}','{}')""".format(self.name, self.office_type)
    
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

    

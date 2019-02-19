"""" Main connection to the postgres database """
import psycopg2
from app.v2.models.database.maindb import set_up_tables


def initdb(db_url):
    """ initialize the class instance to take a database url as a
            parameter"""
    try:
        # global conn, cur
        conn = psycopg2.connect(db_url)
        cur = .conn.cursor()
        tables = set_up_tables()
        for query in tables:
            cur.execute(query)
            print(query)
            conn.commit()
    except Exception as error:
        print(error)






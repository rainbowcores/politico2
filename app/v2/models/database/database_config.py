"""" Main connection to the postgres database """
import json
import psycopg2
from app.v2.models.database.maindb import set_up_tables, drop_tables
from app.v2.models.usersmodel import Users
from app.v2.views.mainview import response
from flask import abort

from flask import current_app as app


def initdb():
    """ initialize the class instance to take a database url as a
            parameter"""
    
    try:
        db_url = app.config["DATABASE_URL"]
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        tables = set_up_tables()
        for query in tables:
            cur.execute(query)
            print(query)
            conn.commit()
        conn.close()
        
    except Exception as error:
        return error


def db_conn():
    try:
        db_url = app.config["DATABASE_URL"]
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        return cur, conn

    except Exception as error:
        return error


def dropdb():
    try:
        db_url = app.config["DATABASE_URL"]
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        tables = drop_tables()
        for query in tables:
            cur.execute(query)
            conn.commit()
            conn.close()
    except Exception as error:
        return error


def query_db(query):
    try:
        cur, conn = db_conn()
        cur.execute(query)
        conn.commit()
        conn.close()
    except Exception as error:
        return error


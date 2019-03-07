from flask import abort
from app.v2.models.modeloffices import Offices
from app.v2.models.usersmodel import Users
from app.v2.models.candidatemodel import Candidates
from app.v2.models.votesmodel import Votes
from app.v2.views.mainview import response
from flask import current_app as app
import psycopg2


class Officemethods:
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
    def get_by_name(name):
        query = """SELECT name, office_type FROM offices WHERE name='{name}';""".format(name=name)
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


class Candidatemethods:
    @staticmethod
    def candidate_registered(candidate, office):
        query = """SELECT * FROM candidates WHERE candidate = '{candidate}' AND office = '{office}'""".format(candidate=candidate, office=office)
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
    def get_by_id(id):
        query = """SELECT * FROM candidates WHERE id='{id}';""".format(id=id)
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
    def get_by_office(office):
        query = """SELECT * FROM candidates WHERE office='{office}';""".format(office=office)
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


class Usermethods:
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

    @staticmethod
    def get_by_id(id):
        query = """SELECT firstname, lastname, nationalid, email, phone_number, passport_url, password FROM users WHERE id='{id}';""".format(id=id)
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


class Votesmethods:
    @staticmethod
    def vote_exists(voter, candidate, office):
        query = """SELECT * FROM votes WHERE voter = '{voter}' AND candidate = '{candidate}' AND office = '{office}'""".format(voter=voter, candidate=candidate, office=office)
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
    def office_has_votes(office):
        query = """SELECT * FROM votes WHERE office = '{office}'""".format(office=office)
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
    def results(office):
        query = """SELECT candidate, COUNT(*) AS office FROM votes WHERE office = {office} GROUP BY candidate, office;""".format(office=office)
        try:
            db_url = app.config["DATABASE_URL"]
            conn = psycopg2.connect(db_url)
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            conn.commit()
            return rows
        except Exception as error:
            return error

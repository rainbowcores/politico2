import psycopg2
from flask import current_app as app


def set_up_tables():
    users = """
                CREATE TABLE IF NOT EXISTS users(
                    id SERIAL PRIMARY KEY,
                    firstname VARCHAR(128) NULL,
                    lastname VARCHAR(128) NULL,
                    nationalid VARCHAR(10) NULL UNIQUE,
                    email VARCHAR(128) NOT NULL,
                    phone_number VARCHAR(10)  NULL,
                    passport_url VARCHAR(256)  NULL,
                    password VARCHAR(256) NOT NULL,
                    is_admin  boolean NOT NULL DEFAULT FALSE,
                    is_politician  boolean NOT NULL DEFAULT FALSE
                );
            """
    parties = """
            CREATE TABLE IF NOT EXISTS parties(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL UNIQUE,
                hq_address VARCHAR(200) NOT NULL,
                logo_url VARCHAR(256) NOT NULL UNIQUE
            );
        """
    offices = """
            CREATE TABLE IF NOT EXISTS offices(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL UNIQUE,
                office_type VARCHAR(100) NOT NULL
            );
        """
    candidates = """
            CREATE TABLE IF NOT EXISTS candidates(
                    id SERIAL,
                    office INTEGER NOT NULL,
                    candidate INTEGER NOT NULL,
                    PRIMARY KEY(office, candidate),
                    FOREIGN KEY (office) REFERENCES offices(id) ON DELETE CASCADE,
                    FOREIGN KEY (candidate) REFERENCES users(id) ON DELETE CASCADE
                );
            """
    votes = """
            CREATE TABLE IF NOT EXISTS votes(
                id SERIAL,
                created_on TIMESTAMP NOT NULL DEFAULT now(),
                voter INTEGER ,
                office INTEGER,
                candidate INTEGER,
                PRIMARY KEY(voter, office),
                FOREIGN KEY (office) REFERENCES offices(id) ON DELETE CASCADE,
                FOREIGN KEY (voter) REFERENCES users(id) ON DELETE CASCADE
            );
        """
    admin = """INSERT INTO users(firstname, lastname, nationalid, email, phone_number, passport_url, password , is_admin, is_politician) VALUES ('FMyAdmin', 'LMyAdmin', '33458802','myadmin@admin.com', '0725355719','adminurl','3668990hh' , True, False);"""
    return [users, parties, offices, candidates, votes, admin]


def drop_tables():
    drop_users = """ DROP TABLE IF EXISTS users CASCADE"""
    drop_parties = """ DROP TABLE IF EXISTS parties CASCADE"""
    drop_offices = """ DROP TABLE IF EXISTS offices CASCADE"""
    drop_candidates = """ DROP TABLE IF EXISTS candidates CASCADE"""
    drop_votes = """ DROP TABLE IF EXISTS votes CASCADE"""

    tables = [drop_users, drop_parties, drop_offices, drop_votes, drop_candidates]
    db_url = app.config["DATABASE_URL"]
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    for query in tables:
        cur.execute(query)
        conn.commit()
    conn.close()

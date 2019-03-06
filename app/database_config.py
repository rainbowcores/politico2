import os
import psycopg2

uri = os.getenv(['DATABASE_URL'])
test_uri = os.getenv(['DATABASE_TEST_URL'])


def connection(url):
    conn = psycopg2.connect(url)
    return conn


def init_db():
    conn = connection(uri)
    curs = conn.cursor()
    queries = tables()

    for query in queries:
        curs.execute(query)
    conn.commit()
    return conn


def init_test_db(test_uri):
    conn = connection(test_uri)
    curs = conn.cursor()
    queries = tables()

    for query in queries:
        curs.execute(query)
    conn.commit()
    return conn


def destoy_db():
    conn = connection(test_uri)
    curs = conn.cursor()

    users = """ DROP TABLE IF EXISTS users CASCADE; """
    parties = """DROP TABLE IF EXISTS parties CASCADE; """
    offices = """DROP TABLE IF EXISTS offices CASCADE; """
    candidates = """DROP TABLE IF EXISTS candidates CASCADE; """
    votes = """DROP TABLE IF EXISTS votes CASCADE; """

    queries = [users, parties, offices, candidates, votes]

    for query in queries:
        curs.execute(query)
    conn.commit()


def tables():
    users = """
                CREATE TABLE users(
                    id SERIAL PRIMARY KEY,
                    firstname VARCHAR NULL,
                    lastname VARCHAR NULL,
                    othername VARCHAR NULL,
                    nationalid VARCHAR(10) NULL UNIQUE,
                    email VARCHAR NOT NULL,
                    phone_number VARCHAR(10)  NULL,
                    passport_url VARCHAR  NULL,
                    password VARCHAR NOT NULL,
                    is_admin  BOOLEAN NOT NULL DEFAULT FALSE
                );
            """
    parties = """
                CREATE TABLE parties(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR NOT NULL UNIQUE,
                    hq_address VARCHAR NOT NULL,
                    logo_url VARCHAR NOT NULL UNIQUE
                );
            """
    offices = """
                CREATE TABLE offices(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL UNIQUE,
                    office_type VARCHAR(100) NOT NULL
                );
            """
    candidates = """
            CREATE TABLE candidates(
                    id SERIAL PRIMARY KEY,
                    office INTEGER,
                    candidate INTEGER,
                    PRIMARY KEY(office,candidate)
                    FOREIGN KEY(office) REFERENCES offices(id) ON DELETE CASCADE,
                    FOREIGN KEY(candidate) REFERENCES users(id) ON DELETE CASCADE
                );
            """
    votes = """
                CREATE TABLE votes(
                    id SERIAL PRIMARY KEY,
                    created_on TIMESTAMP NOT NULL DEFAULT now(),
                    voter INTEGER,
                    office INTEGER,
                    candidate INTEGER,
                    PRIMARY KEY (voter, office)
                    FOREIGN KEY(voter) REFERENCES users(id) ON DELETE CASCADE,
                    FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE,
                    FOREIGN KEY(candidate_id) REFERENCES users(id) ON DELETE CASCADE
                );
            """
    queries = [users, parties, offices, candidates, votes]
    return queries

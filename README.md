# Politico API
___
The general elections are around the corner, hence it’s a political season. Get into the mood of
the season and help build a platform which both the politicians and citizens can use.
Politico enables citizens give their mandate to politicians running for different government offices
while building trust in the process through transparency.


[![Build Status](https://travis-ci.org/rainbowcores/politico2.svg?branch=develop)](https://travis-ci.org/rainbowcores/politico2) [![Coverage Status](https://coveralls.io/repos/github/rainbowcores/politico2/badge.svg?branch=ch-validations-tests-163781483)](https://coveralls.io/github/rainbowcores/politico2?branch=ch-validations-tests-163781483) [![Maintainability](https://api.codeclimate.com/v1/badges/88e335ce50be8a72dc27/maintainability)](https://codeclimate.com/github/rainbowcores/politico2/maintainability) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/0733351c38ca40749dbce07eaa402de8)](https://www.codacy.com/app/rainbowcores/politico2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rainbowcores/politico2&amp;utm_campaign=Badge_Grade)

## Requirements to Install
+ Python
## Installation Steps
+ Clone this repo by 

`git clone https://github.com/rainbowcores/politico2.git`

+ Change directory to the project folder 

`cd Politico2`

+ Create a virtual environment 

`virtualenv venv`

+ Activate the virtual environment

`. venv/bin/activate`

+ Install dependencies 

`pip install -r requirements.txt`

## Start the server and run the application

`flask run`
___

# API Endpoints
## Heroku - https://politico-christine.herokuapp.com

| Method  |  Route  | Functionality   |
|---|---|---|
| POST  | `/api/v1/politicalparties`  | Creates new political party  |
| GET  | `/api/v1/politicalparties`  |  Get all political parties |
| GET  |  `/api/v1/politicalparties/<int:party_id>` |  Get a specific political party |
| DELETE  |  `/api/v1/politicalparties/<int:party_id>` | Delete a specific political party  |
|  PATCH | `/api/v1/politicalparties/<int:party_id>`  | Edit the name of a specific political party  |
|  POST | `/api/v1/politicaloffices` |  Create a new political office |
| GET  |  `/api/v1/politicaloffices` |  Get all political offices |
| GET  | `/api/v1/politicaloffices/<int:office_id>`  | Get a specific political office  |
___
# Test the API
#### Test the API Endpoints
Use any REST Client such as [Postman](https://www.getpostman.com/) or [Insomnia](https://insomnia.rest/)

### Run Unit Tests

`pytest --cov=app  tests/`
___
# Author

##### Christine Wanjiru

___


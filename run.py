import os

from app import create_app

#config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app('development')

@app.route('/')
def hello():
    return 'Welcome to Politico'

if __name__ == '__main__':
    app.run()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object('config.ProdConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app, db)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
def main():
    return "Hello Word"


def make_app():
    from api.doctors import doctors
    from api.addresses import addresses

    app.register_blueprint(doctors)
    app.register_blueprint(addresses)
    return app

if __name__ == '__main__':
    app = make_app()
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.LocalConfig')
db = SQLAlchemy(app)


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

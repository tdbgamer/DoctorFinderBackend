from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.LocalConfig')
db = SQLAlchemy(app)


@app.route('/')
def main():
    return "Hello Word"


if __name__ == '__main__':
    from api.doctors import doctors
    from api.addresses import addresses

    app.register_blueprint(doctors)
    app.register_blueprint(addresses)
    app.run(debug=True)

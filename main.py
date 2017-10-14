from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object('config.ProdConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app, db)
manager.add_command('db', MigrateCommand)


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

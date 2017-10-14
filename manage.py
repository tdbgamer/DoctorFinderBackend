from flask import current_app
from flask_migrate import MigrateCommand
from main import manager
import csv

if __name__ == '__main__':
    from models import *

    manager.add_command('db', MigrateCommand)

    @manager.command
    def insert_data():
        with open('fake_data.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # do stuff


    manager.run()

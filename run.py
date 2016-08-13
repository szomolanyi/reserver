#!/usr/bin/env python 

from flask_script import Manager, Shell
from app import create_app, db
from app.user import model
from pprint import pprint
from unittest import TestLoader, TextTestRunner


app = create_app('default')

def _make_context():
    app = create_app('default')
    return dict(app=app, db=db, user_model=model)

manager = Manager(app)

manager.add_command("shell", Shell(make_context=_make_context, use_ipython=True ))

@manager.command
def routes():
    "Displays all routes"
    app = create_app('test')
    print (db.engine)
    pprint(app.url_map)

@manager.command
def check():
    "Run all tests"
    tests = TestLoader().discover('./tests')
    TextTestRunner(verbosity=2).run(tests)

@manager.command
def create_db():
    "Creates database"
    db.create_all()

if __name__ == "__main__":
    manager.run()

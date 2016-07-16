import unittest
import os

from app import db, app
from app.user.model import EmailLogin, Provider
from config import basedir


class UserTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def testProvider1(self):
        p = Provider(name="Pneuservis a.s.")
        u = EmailLogin(email="dd@gmail.com", token="topsecret")
        p.email_login_ = u
        db.session.add(p)
        db.session.add(u)
        db.session.commit()
        p1 = Provider(name="Kadernictvo s.r.o")
        db.session.add(p1)
        db.session.commit()
        providers = Provider.query.filter_by(name="Pneuservis a.s.")
        for pr in providers:
        	print "Provider name = {}, email_login = {}".format(pr.name, pr.email_login_.email)
        providers = Provider.query.filter_by(name="Kadernictvo s.r.o.")
        for pr in providers:
            print "Provider name = {}, email_login = {}".format(pr.name, pr.email_login_.email)
        emails = EmailLogin.query.all()
        for e in emails:
            print "EmailLogin email = {}, provider name = {}".format(e.email, e.provider_.name)
        email = EmailLogin.query.filter_by(email="dd@gmail.com")[0]
        pr = email.provider_
        print("Provider by email [{}] : {}").format(email.email, pr.name)

    def _testProvider2(self):
        p = Provider(name="Kadernictvo")
        db.session.add(p)
        providers = Provider.query.all()
        for pr in providers:
            print "Provider name = {}".format(pr.name)

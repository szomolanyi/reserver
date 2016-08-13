import unittest
import os

from flask import url_for
from app import db, create_app
from app.user.model import EmailLogin, User
from config import basedir


class UserTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
        db.create_all()
        self.user = User()
        db.session.add(self.user)
        db.session.flush()
        self.email_login = EmailLogin(
            email="test@test.sk", password='Heslo', user_id=self.user.id)
        db.session.add(self.email_login)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def testPasswordHashed(self):
        self.assertNotEqual(self.email_login.password_hash, 'Heslo')
        self.assertNotEqual(self.email_login.password_hash, 'Heslo')
        self.assertFalse(self.email_login.verify_password('Heslo1'))
        self.assertTrue(self.email_login.verify_password('Heslo'))
        with self.assertRaises(AttributeError):
            self.email_login.password

    def login(self, email, password):
        return self.client.post(url_for('user.login'), data={
            'email': email,
            'password': password}, follow_redirects=True)

    def testLogin(self):
        self.assertIn("Invalid username or password",
                      self.login('not@exists.sk', 'wrong').data)
        self.assertIn("Logout", self.login('test@test.sk', 'Heslo').data)

    def register(self, email, password, password2):
        return self.client.post(url_for('user.register'), data={
            'email': email,
            'password': password,
            'password2': password2
        })

    def testRegister(self):
        self.assertEqual(self.register(
            email=None, password=None,
            password2=None).data.count('This field is required'), 3)
        self.assertIn("Invalid email address", self.register(
            email='ddd', password='aaaaaaaa', password2='aaaaaaaa').data)
        self.assertIn('Field must be equal to password', self.register(
            email='d@d.sk', password='1', password2='2').data)
        self.assertIn('Field must be between 8 and 50 characters long', self.register(
            email='d@d.sk', password='aaaa', password2='aaaa').data)

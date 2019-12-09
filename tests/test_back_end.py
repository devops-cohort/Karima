import unittest

from flask import abort, url_for
from flask_testing import TestCase

from os import getenv

from application import app, db

from application.models import Users, Posts


class TestBase(TestCase):

    def create_app(self):
    
        #pass in test configurations
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MY_SQL_USER'))+':'+str(getenv('MY_SQL_PASSWORD'))+'@'+str(getenv('MY_SQL_URL'))+'/'+str(getenv('MY_SQL_DB')))
        return app

    def setup(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        #Create test admin user

        admin = Users(first_name="admin",last_name="admin", email="admin@admin.com", password="admin101")

        #Create test non admin user

        employee = Users(first_name="test",last_name="test", email="test@user.com", password="test101")

        #save users to database

        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def teardown(self):

        db.session.remove()
        db.drop_all()



class allthetests(TestBase):

    def test_page(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


    def test_page(self):
        
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)



    def test_user_view(self):

        targer_url = url_for('create', user_id=1)
        redirect_irl = url_for('login', next=target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,redirect_url)


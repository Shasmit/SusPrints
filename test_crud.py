from email import header
from http import client
from flask import Flask
import unittest
import json
# from urllib3 import urlencode
from multidimensional_urlencode import urlencode
# import werkzeug
from app import app as create_app

class FlaskTest(unittest.TestCase):
# Normal login get test
    def test_base_route(self):
        # app = Flask(__name__)
        app = create_app
        # app.register_blueprint(auth, url_prefix="/")
        # app.iter_blueprints
        client = app.test_client()
        url = '/login'

        response = client.get(url)
        # assert response.get_data() == b'Hello, World!'
        assert response.status_code == 200
        
    # Login successfull test
    def test_login(self):
        # app = Flask(__name__)
        app = create_app
        # app.register_blueprint(auth, url_prefix="/")
        # app.iter_blueprints
        client = app.test_client()
        url = '/login'
        
        mockRequestHeaders={
            "Content-Type": "application/x-www-form-urlencoded"
        }

        mockData = urlencode({
            "email": "shasmitkoarko@email.com",
            "password": "asdfghjklsaaj,hvzjh",
        })

        response = client.post(url,data=mockData,headers=mockRequestHeaders)
        # assert response.get_data() == b'Hello, World!'
        print(response.data)
        assert response.status_code == 200

    # # Create new account
    # def test_signup(self):
    #     app = create_app
    #     client = app.test_client()
    #     url = '/register'
        
    #     mockRequestHeaders={
    #         "Content-Type": "application/x-www-form-urlencoded"
    #     }

    #     mockData = urlencode({
    #         "user1": "Qubitsq",
    #         "email2": "qubititi@sus.com",
    #         "password1": "binod123454"
    #     })

    #     response = client.post(url,data=mockData,headers=mockRequestHeaders)
    #     assert response.status_code == 201

if __name__ == "__main__":
    unittest.main()

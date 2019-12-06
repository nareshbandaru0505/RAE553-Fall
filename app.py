# Flask class is imported from flask module
from flask import Flask, request
# abort, Resource, Api classes imported from flask_restful module inorder to create the first rest api
from flask_restful import Resource, Api, abort, reqparse

#import JWT,jwt_required, current_identity from flask_jwt module which is used for authentication
from flask_jwt import JWT, jwt_required, current_identity

#import authenticate and identity from securty.py previously created.
from security import authenticate, identity
from user import UserRegister
from item import Item

# Flask application instance is created using below command
app = Flask(__name__)

# Adding a secreate line
app.secret_key = 'FirstJson1'

#Api application instance is created using below command
api = Api(app)

#create a JWT object. As soon as this JWT object created, Flask-JWT registers an endpoint with our application, /auth
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/<name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)

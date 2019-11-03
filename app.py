# Flask class is imported from flask module
from flask import Flask, request
# abort, Resource, Api classes imported from flask_restful module inorder to create the first rest api
from flask_restful import Resource, Api, abort

from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity

# Flask application instance is created using below command
app = Flask(__name__)

# Adding a secreate line
#app.config['SECRET_KEY'] = 'FirstJson1'
app.secret_key = 'FirstJson1'

#Api application instance is created using below command
api = Api(app)

jwt = JWT(app, authenticate, identity)

#defining total items
items = {}

# generally API works with resources and resoruces should be defined as class. item and itemList is created as Resource class
# Resource item definition
# for GET and DELETE method, verifying if the  value exists. if doesnt exists, report error code 404 and print itemX doesnt exist message line 14
class item(Resource):
    # GET method to print an specific item
    # if the requted item doesnt exist, it will abort with an error with code 404
    @jwt_required()
    def get(self, name):
        if name in items:
            return {name: items[name]}
        else:
            abort(404, message="{} doesn't exist".format(name))
 
    #put method to create a new item or modify the existing
    @jwt_required()
    def put(self, name):
        items[name] = {'price' : request.form['price'] }
        return {name: items[name]}

    # POST method to create a new endpoint with concrete price value as requested.
    # if the requted name already exist, it will abort and  print an error with error code 403
    @jwt_required()
    def post(self, name):
        if name not in items:
            items[name] = { 'price' : '500' }
            return {name: items[name]}
        else:
            abort(403, message="{} exist".format(name))
    # DELETE method to DEleTE an specific item
    # if the requted item doesnt exist, it will abort with an error with code 404
    @jwt_required()
    def delete(self, name):
        if name in items:
            del items[name]
            return name + " is deleted"
        else:
            abort(404, message="{} doesn't exist".format(name))

# itemList
# shows a list of all total_items, and lets you POST to add new tasks
# get method to print all the items

class itemList(Resource):
    @jwt_required()
    def get(self):
        return items

##
##  setup the Api resources routing
##

api.add_resource(item, '/items/<name>')
api.add_resource(itemList, '/items')

if __name__ == '__main__':
    app.run(debug=True)

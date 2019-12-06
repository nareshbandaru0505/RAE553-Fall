
from flask_restful import Resource, Api, abort, reqparse
from flask_jwt import JWT, jwt_required, current_identity

import sqlite3

# generally API works with resources and resoruces should be defined as class. item and itemList is created as Resource class
# Resource item definition
# for GET and DELETE method, verifying if the  value exists. if doesnt exists, report error code 404 and print itemX doesnt exist message line 14
# Inside any endpoint that is decorated with @jwt_required(), can access the current_identity proxy—
# it will give us whatever the identity function returns for the JWT we received in this specific request.

class Item(Resource):
    TABLE_NAME = 'items'
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float,required=True, help='This field cannot be left blank')
    # GET method to print an specific item
    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message':'Item not found'}, 404
    # POST method to print an specific item
    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {"message": "An item with name '{}' already exists".format(name)}
        data = Item.parser.parse_args()
        item = {'name': name, 'price':data['price']}
        try:
            Item.insert(item)
        except:
            return {"message":"An error occured during inserting item"}, 500
        return item, 201
        # PUT method to print an specific item
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        update_item = {'name': name, 'price':data['price']}
        if item is None:
            try:
                Item.insert(update_item)
            except:
                return {"message":"an error occured during update an item"}
        else:
            try:
                Item.update(update_item)
            except:
                raise
                return {"message":"an error occured during update an item"}
        return update_item

    # finding the item in the list
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME) # verify the item if it exists
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'item': {'name':row[0], 'price':row[1]}} #return the item if it exists

    # definition of insert for POST and PUT methods
    @classmethod
    def insert(cls, item):
        #connection to database
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        #query the database
        query = "INSERT INTO {table} VALUES (?,?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['name'],item['price']))
        connection.commit() #commit and close the db access
        connection.close()
        return {'message':'Item Added'}   

    #update method for PUT methods
    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['price'],item['name']))
        connection.commit()
        connection.close()
        return {'message':'Item Updated'}   
    #DELETE METHOD
    @jwt_required()
    def delete(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message':'Item Deleted'}   


from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

actions = {}

class Student(Resource):
    def get(self, name):
        return {name: actions[name]}

    def put(self, name):
        actions[name] = request.form['data']
        return {name: actions[name]}

    def delete(self, name):
        del actions[name]
        return 'DELETED'

api.add_resource(Student, '/student/<string:name>')

if __name__ == '__main__':
    app.run()

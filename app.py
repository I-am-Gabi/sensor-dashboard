from flask import Flask, Blueprint, render_template, jsonify
from flask_restful import Api, Resource, url_for, reqparse

##
## Setup the API
##
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

parser = reqparse.RequestParser()
parser.add_argument('sensor1')
parser.add_argument('sensor2')
parser.add_argument('sensor3')
parser.add_argument('sensor4')

field1 = field2 = field3 = field4 = 0


class Sensor(Resource):
    def post(self):
        global field1, field2, field3, field4
        args = parser.parse_args()
        field1 = args['sensor1']
        field2 = args['sensor2']
        field3 = args['sensor3']
        field4 = args['sensor4']
        return '', 201


api.add_resource(Sensor, '/update')

##
## Setup the App
##
app = Flask(__name__)
app.register_blueprint(api_bp)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/sensor_data", methods=['GET'])
def sensor_data():
    return jsonify(sensor1=field1, sensor2=field2, sensor3=field3, sensor4=field4)


if __name__ == "__main__":
    app.run()

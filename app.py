from flask import Flask, Blueprint, render_template
from flask_restful import Api, Resource, url_for, reqparse

##
## Setup the API
##
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

parser = reqparse.RequestParser()
parser.add_argument('field')

field = None


class Sensor(Resource):
    def post(self):
        global field
        args = parser.parse_args()
        field = args['field']
        return '', 201


api.add_resource(Sensor, '/update')

##
## Setup the App
##
app = Flask(__name__)
app.register_blueprint(api_bp)


@app.route("/")
def hello():
    return render_template('index.html', content=field)


if __name__ == "__main__":
    app.run()

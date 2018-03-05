from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS
from flasgger import Swagger

from security import authenticate, identity
from resources.user import UserRegister
from resources.customer import Customer, CustomerList
from resources.score import Score, ScoreList

app = Flask(__name__)
#cors = CORS(app)
cors = CORS(app, resorces={r'/*': {"origins": '*'}})
app.config['CORS_HEADERS'] = 'application/json'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'EiEiO'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


app.config['SWAGGER'] = {
    "uiversion": 3,
    "swagger_version": "3.0",
    "title": "Serasa API",
    "specs_route": "/serasa-api-docs/",
    "description": "This is the version 1 serasa API",
}

Swagger(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Score, '/score/<string:type_risk>')
api.add_resource(ScoreList, '/scores')
api.add_resource(Customer, '/customer/<string:tax_id>')
api.add_resource(CustomerList, '/customers')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=80, debug=True)

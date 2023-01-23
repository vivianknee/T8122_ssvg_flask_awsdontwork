from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.cars import Car

car_api = Blueprint('car_api', __name__,
                   url_prefix='/api/cars')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(car_api)

class CarAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate type
            type = body.get('type')
            if type is None or len(type) < 2:
                return {'message': f'type is missing, or is less than 2 characters'}, 210
            # validate uid
            model = body.get('model')
            if model is None or len(model) < 2:
                return {'message': f'car ID is missing, or is less than 2 characters'}, 210
            # look for password and dob
            price = body.get('price') 

            ''' #1: Key code block, setup car OBJECT '''
            co = Car(type=type, 
                      model=model,
                      price=price)
            
            
            ''' #2: Key Code block to add car to database '''
            # create car in database
            car = co.create()
            # success returns json of car
            if car:
                return jsonify(car.read())
            # failure returns error
            return {'message': f'Processed {type}, either a format error or model {model} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            cars = Car.query.all()    # read/extract all cars from database
            json_ready = [car.read() for car in cars]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
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
            
            brand = body.get('brand')
            if brand is None or len(brand) < 2:
                return {'message': f'brand is missing, or is less than 2 characters'}, 210
             
            color = body.get('color')
            if color is None or len(color) < 2:
                return {'message': f'color is missing, or is less than 2 characters'}, 210
            
            type = body.get('type')
            if type is None or len(type) < 2:
                return {'message': f'type is missing, or is less than 2 characters'}, 210
             
            powersource = body.get('powersource')
            if powersource is None or len(powersource) < 2:
                return {'message': f'powersource is missing, or is less than 2 characters'}, 210
            
            price_range = body.get(price_range) 
            if price_range is None or len(price_range) < 2:
                return {'message': f'powersource is missing, or is less than 2 characters'}, 210
         
            ''' #1: Key code block, setup car OBJECT '''
            co = Car(type=type, 
                      engine=engine,
                      price=price)
            
            ''' #2: Key Code block to add car to database '''
            # create car in database
            car = co.create()
            # success returns json of car
            if car:
                return jsonify(car.read())
            # failure returns error
            return {'message': f'Processed {type}, either a format error or engine {engine} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            cars = Car.query.all()    # read/extract all cars from database
            json_ready = [car.read() for car in cars]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.carspecs import CarSpecs

carspec_api = Blueprint('carspec_api', __name__,
                   url_prefix='/api/carspec')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(carspec_api)

class CarSpecsAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            name = body.get('name')
            if name is None or len(name) < 1:
                return {'message': f'name is missing, or is less than 2 characters'}, 210
             
            type = body.get('type')
            if type is None or len(type) < 1:
                return {'message': f'type is missing, or is less than 2 characters'}, 210
            
            seatingCapacity = body.get('seatingCapacity')
            if seatingCapacity is None or len(seatingCapacity) < 1:
                return {'message': f'seatingCapacity is missing, or is less than 2 characters'}, 210
             
            powerSource = body.get('powerSource')
            if powerSource is None or len(powerSource) < 1:
                return {'message': f'powerSource is missing, or is less than 2 characters'}, 210
            
            transmission = body.get(transmission) 
            if transmission is None or len(transmission) < 1:
                return {'message': f'transmission is missing, or is less than 2 characters'}, 210
            
            mileage = body.get(mileage) 
            if mileage is None or len(mileage) < 1:
                return {'message': f'mileage is missing, or is less than 2 characters'}, 210
            
            range = body.get(range) 
            if range is None or len(range) < 1:
                return {'message': f'range is missing, or is less than 2 characters'}, 210
         
            ''' #1: Key code block, setup car OBJECT '''
            co = CarSpecs(name=name,
                      type=type,
                      seatingCapacity=seatingCapacity, 
                      powerSource=powerSource,
                      transmission=transmission,
                      mileage=mileage,
                      range=range)
            
            ''' #2: Key Code block to add car to database '''
            # create car in database
            carspec = co.create()
            # success returns json of car
            if carspec:
                return jsonify(carspec.read())
            # failure returns error
            return {'message': f'Processed {type}, either a format error or powerSource {powerSource} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            carspecs = CarSpecs.query.all()    # read/extract all cars from database
            json_ready = [carspec.read() for carspec in carspecs]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
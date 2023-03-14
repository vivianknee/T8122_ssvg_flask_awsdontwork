from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.dealerships import Dealership

dealership_api = Blueprint('dealership_api', __name__,
                   url_prefix='/api/dealerships')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(dealership_api)

class DealershipAPI:
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            distance = body.get('distance')
            if distance is None or len(distance) < 2:
                return {'message': f'distance is missing, or is less than 2 characters'}, 210
             
            zip = body.get('zip')
            if zip is None or len(zip) < 2:
                return {'message': f'zip is missing, or is less than 2 characters'}, 210
             
            brand = body.get('brand')
            if brand is None or len(brand) < 2:
                return {'message': f'brand is missing, or is less than 2 characters'}, 210
            
            location = body.get('location')
            if location is None or len(location) < 2:
                return {'message': f'location is missing, or is less than 2 characters'}, 210

            ''' #1: Key code block, setup car OBJECT '''
            co = dealership(distance=distance,
                      zip=zip,
                      brand=brand, 
                      location=location)
            
            ''' #2: Key Code block to add dealership to database '''
            # create dealership in database 
            dealership = co.create()
            # success returns json of dealership
            if dealership:
                return jsonify(dealership.read())
            # failure returns error
            return {'message': f'Processed {type}, either a format error or brand {brand} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            dealerships = Dealership.query.all()    # read/extract all cars from database
            json_ready = [dealership.read() for dealership in dealerships]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
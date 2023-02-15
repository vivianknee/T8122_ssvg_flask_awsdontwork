""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class CarSpecs(db.Model):
    __tablename__ = 'carspecs'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, unique=True, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _type = db.Column(db.String(255), unique=False, nullable=False)
    _seatingCapacity = db.Column(db.String(255), unique=False, nullable=False)
    _powerSource = db.Column(db.String(255), unique=False, nullable=False)
    _transmission = db.Column(db.String(255), unique=False, nullable=False)
    _mileage = db.Column(db.String(255), unique=False, nullable=False)
    _range = db.Column(db.String(255), unique=False, nullable=False)
   

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, type, seatingCapacity, powerSource, transmission, mileage, range):
        self._name = name   # variables with self prefix become part of the object, 
        self._type = type
        self._seatingCapacity = seatingCapacity
        self._powerSource = powerSource
        self._transmission = transmission
        self._mileage = mileage
        self._range = range 
        #self.determine_value()

    # gets the name of the car
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name

     # gets the type of the car
    @property
    def type(self):
        return self._type
    
    # a setter function, allows type to be updated after initial object creation
    @type.setter
    def type(self, type):
        self._type = type 

    # gets the type of the seating capacity of the car
    @property
    def seatingCapacity(self):
        return self._seatingCapacity
    
    # a setter function, allows seating capacity to be updated after initial object creation
    @seatingCapacity.setter
    def seatingCapacity(self, seatingCapacity):
        self._seatingCapacity = seatingCapacity
    
    # a powerSource getter
    @property
    def powerSource(self):
        return self._powerSource

    # a setter function to set the car's powerSource
    @powerSource.setter
    def powerSource(self, powerSource):
        self._powerSource = powerSource
    
     # a transmission getter
    @property
    def transmission(self):
        return self._transmission

    # a setter function to set the car's transmission
    @transmission.setter
    def transmission(self, transmission):
        self._transmission = transmission
        
     # a mileage getter
    @property
    def mileage(self):
        return self._mileage

    # a setter function to set the car's mileage
    @mileage.setter
    def mileage(self, mileage):
        self._mileage = mileage
    
     # a range getter
    @property
    def range(self):
        return self._range

    # a setter function to set the car's mileage
    @range.setter
    def range(self, range):
        self._range = range        
            
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "name" : self.name,
            "type" : self.type,
            "seatingCapacity" : self.seatingCapacity,
            "powerSource" : self.powerSource,
            "transmission" : self.transmission,
            "mileage" : self.mileage,
            "range" : self.range
           # "value" : self.value
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, name="", type="", seatingCapacity="", powerSource="", transmission="", mileage="", range=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(type) > 0:
            self.type = type
        if len(seatingCapacity) > 0:
            self.seatingCapacity = seatingCapacity
        if len(powerSource) > 0:
            self.powerSource = powerSource
        if len(transmission) > 0:
            self.transmission = transmission
        if len(mileage) > 0:
            self.mileage = mileage
        if len(range) > 0:
            self.range = range
        # self.price_range = price_range
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """

# Builds working data for testing

def initCarSpec():
    """Create database and tables"""
    db.create_all()

    try:
        db.session.query(CarSpecs).delete()
        db.session.commit()
    except:
        db.session.rollback()

    """Tester data for table""" 
    s1 = CarSpecs(name='Chevrolet Blazer', type='SUV', seatingCapacity='5', powerSource='Gasoline', transmission='Automatic', mileage='b', range='Non-Electric')
    s2 = CarSpecs(name='Chevrolet Blazer EV', type='SUV', seatingCapacity='5', powerSource='Electric', transmission='Automatic', mileage='Non-Gasoline', range='3') 
    s3 = CarSpecs(name='Chevrolet Bolt EV', type='SUV', seatingCapacity='5', powerSource='Electric', transmission='Automatic', mileage='Non-Gasoline', range='Non-Electric')
    s4 = CarSpecs(name='Chevrolet Equinox', type='SUV', seatingCapacity='5', powerSource='Gasoline', transmission='Automatic', mileage='b', range='Non-Gasoline')
    s5 = CarSpecs(name='Chevrolet Equinox EV', type='SUV', seatingCapacity='5', powerSource='Electric', transmission='Automatic', mileage='Non-Gasoline', range='2')
    s6 = CarSpecs(name='Chevrolet Trailblazer', type='SUV', seatingCapacity='5', powerSource='Gasoline', transmission='Automatic', mileage='b', range='Non-Electric') 
    s7 = CarSpecs(name='Chevrolet Traverse', type='SUV', seatingCapacity='7', powerSource='Gasoline', transmission='Automatic', mileage='b', range='Non-Electric')
    s8 = CarSpecs(name='Chevrolet Seeker', type='SUV', seatingCapacity='5', powerSource='Gasoline', transmission='Automatic', mileage='c', range='Non-Electric')
    s9 = CarSpecs(name='Chevrolet Suburban', type='SUV', seatingCapacity='8', powerSource='Gasoline', transmission='Automatic', mileage='a', range='Non-Electric')
    s10 = CarSpecs(name='Chevrolet Tahoe', type='SUV', seatingCapacity='8', powerSource='Gasoline', transmission='Automatic', mileage='a', range='Non-Electric') 
    s11 = CarSpecs(name='Chevrolet Colorado', type='Pickup Truck', seatingCapacity='5', powerSource='Gasoline', transmission='Automatic', mileage='a', range='Non-Electric')

    carspecs = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]

    """Builds sample car/note(s) data""" # NEEDS TO CONNECT TO CARSPEC.PY FILE THAT BUILDS THE API
    for carspec in carspecs:
        try:
            carspec.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {carspec.model}")


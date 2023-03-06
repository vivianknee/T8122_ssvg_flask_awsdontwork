""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError



class Dealership(db.Model):
    __tablename__ = 'dealerships'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, unique=True, primary_key=True)
    _distance = db.Column(db.String(255), unique=False, nullable=False)
    _zip = db.Column(db.Integer, unique=False, nullable=False)
    _brand = db.Column(db.String(255), unique=False, nullable=False)
   

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, distance, zip, brand):
        self._distance = distance    # variables with self prefix become part of the object, 
        self._zip = zip
        self._brand = brand
        #self.determine_value()

    # gets the distance from the dealership
    @property
    def distance(self):
        return self._distance
    
    # a setter function, allows brand to be updated after initial object creation
    @distance.setter
    def distance(self, distance):
        self._distance = distance

     # gets the zip of the user
    @property
    def zip(self):
        return self._zip
    
    # a setter function, allows color to be updated after initial object creation
    @zip.setter
    def zip(self, zip):
        self._zip = zip
    
    # a powersource getter
    @property
    def brand(self):
        return self._brand

    # a setter function to determine user's brand of choice
    @brand.setter
    def brand(self, brand):
        self._brand = brand
         
    # @property
    # def value(self):
    #     return self._value
            
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
            "distance" : self.distance,
            "zip" : self.zip,
            "brand" : self.brand
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, distance="", zip="", brand=""):
        """only updates values with length"""
        if len(distance) > 0:
            self.distance = distance
        if len(zip) > 0:
            self.zip = zip
        if len(brand) > 0:
            self.brand = brand
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """
def initDealerships():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()

        try:
            db.session.query(Dealership).delete()
            db.session.commit()
        except:
            db.session.rollback()

        d1 = Dealership(distance='10 miles', zip='92127', brand='honda')
        d2 = Dealership(distance='10 miles', zip='92127', brand='hyundai')
        d3 = Dealership(distance='10 miles', zip='92127', brand='toyota')
        d4 = Dealership(distance='10 miles', zip='92127', brand='chevrolet')
        d5 = Dealership(distance='10 miles', zip='92127', brand='lexus')
        d6 = Dealership(distance='10 miles', zip='92127', brand='tesla')
        d7 = Dealership(distance='10 miles', zip='92127', brand='ferrari')
        d8 = Dealership(distance='10 miles', zip='92127', brand='mercedes')
        d9 = Dealership(distance='10 miles', zip='92127', brand='kia')
        d10 = Dealership(distance='10 miles', zip='92127', brand='mazda')
        d11 = Dealership(distance='10 miles', zip='92127', brand='nissan')
        d12 = Dealership(distance='10 miles', zip='92127', brand='jeep')
        d13 = Dealership(distance='10 miles', zip='92127', brand='acura')
        d14 = Dealership(distance='10 miles', zip='92127', brand='dodge')
        d15 = Dealership(distance='10 miles', zip='92127', brand='ford')
        d16 = Dealership(distance='10 miles', zip='92127', brand='subaru')
        d17 = Dealership(distance='10 miles', zip='92127', brand='audi')
        d18 = Dealership(distance='10 miles', zip='92127', brand='BMW')

        dealerships = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18]

        """Builds sample dealership/note(s) data"""
        for dealership in dealerships:
            try:
                dealership.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {dealership.model}")


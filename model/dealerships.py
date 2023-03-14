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
    _location = db.Column(db.String(255), unique=False, nullable=False)
   

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, distance, zip, brand, location):
        self._distance = distance    # variables with self prefix become part of the object, 
        self._zip = zip
        self._brand = brand
        self._location = location 
        #self.determine_value()

    # gets the distance from the dealership
    @property
    def distance(self):
        return self._distance
    
    # a setter function, allows distance to be updated after initial object creation
    @distance.setter
    def distance(self, distance):
        self._distance = distance

     # gets the zip of the user
    @property
    def zip(self):
        return self._zip
    
    # a setter function, allows ZIP to be updated after initial object creation
    @zip.setter
    def zip(self, zip):
        self._zip = zip
    
    # a brand getter
    @property
    def brand(self):
        return self._brand

    # a setter function to determine user's brand of choice
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def location(self, location):
        return self._location 

    @brand.setter
    def location(self, location):
        self._location = location 
         
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
            "brand" : self.brand,
            "location": self.location
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, distance="", zip="", brand="", location=""):
        """only updates values with length"""
        if len(distance) > 0:
            self.distance = distance
        if len(zip) > 0:
            self.zip = zip
        if len(brand) > 0:
            self.brand = brand
        if len(location) > 0:
            self.location = location
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

        d1 = Dealership(distance='10 miles', zip='92127', brand='honda', location='13747 Poway Road, Poway, CA 92064')
        d2 = Dealership(distance='10 miles', zip='92127', brand='hyundai', location='13910 Poway Road, Poway, CA 92064')
        d3 = Dealership(distance='10 miles', zip='92127', brand='toyota', location='13631 Poway Road, Poway, CA 92064')
        d4 = Dealership(distance='10 miles', zip='92127', brand='chevrolet', location='1550 Auto Park Way, Escondido, CA 92029')
        d5 = Dealership(distance='10 miles', zip='92127', brand='lexus', location='1205 Auto Park Way, Escondido, CA 92029')
        d6 = Dealership(distance='10 miles', zip='92127', brand='mercedes', location='855 La Terraza Blvd, ESCONDIDO, CA 92025')
        d7 = Dealership(distance='10 miles', zip='92127', brand='kia', location='1501 Auto Park Way, Escondido, CA 92029')
        d8 = Dealership(distance='10 miles', zip='92127', brand='mazda', location='1560 Auto Parkway, Escondido, CA 92029')
        d9 = Dealership(distance='10 miles', zip='92127', brand='nissan', location='14100 Poway Road, Poway, CA 92064')
        d10 = Dealership(distance='10 miles', zip='92127', brand='jeep', location='13811 Poway Road, Poway, CA 92064')
        d11 = Dealership(distance='10 miles', zip='92127', brand='acura', location='1502 Auto Park Way North, Escondido, CA 92029')
        d12 = Dealership(distance='10 miles', zip='92127', brand='dodge', location='13811 Poway Road, Poway, CA 92064')
        d13 = Dealership(distance='10 miles', zip='92127', brand='ford', location='12740 Poway Rd, Poway, CA 92064')
        d14 = Dealership(distance='10 miles', zip='92127', brand='audi', location='1556 Auto Park Way North, Escondido, CA 92029')
        d15 = Dealership(distance='10 miles', zip='92127', brand='BMW', location='1557 Auto Park Way, Escondido, CA 92029')

        dealerships = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15]

        """Builds sample dealership/note(s) data"""
        for dealership in dealerships:
            try:
                dealership.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {dealership.model}")


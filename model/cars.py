""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Car(db.Model):
    __tablename__ = 'cars'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _color = db.Column(db.String(255), unique=False, nullable=False)
    _price = db.Column(db.Integer, unique=False, nullable=False)
   

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, color, price):
        self._name = name    # variables with self prefix become part of the object, 
        self._color = color
        self._price = price
        self.determine_value()

    # gets the name of the manufacturer or the car
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    
    # a color getter
    @property
    def color(self):
        return self._color

    # a setter function to set the car's color
    @color.setter
    def color(self, color):
        self._color = color
    
     # a price getter
    @property
    def price(self):
        return self._price

    # a setter function to set the car's price 
    @price.setter
    def price(self, price):
        self._price = price
        self.determine_value() #calls function whenever price of car changes 
         
    @property
    def value(self):
        return self._value
    
    #determines car value based on price and stores it by assigning it to object
    def determine_value(self):
        if self._price > 60000:
            self._value = "Luxury Car"
        elif self._price in range(30000, 60000):
            self._value ="Middle-end Car"
        else:
            self._value ="Low-end/Second-hand Car"
            
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
            "color" : self.color,
            "price" : self.price,
            "value" : self.value
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, name="", color="", price=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(color) > 0:
            self.color = color
        self.price = price
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
def initCars():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    u1 = Car(name='Thomas Edison', color='toby', price=7)
    u2 = Car(name='Nicholas Tesla', color='niko', price=7)
    u3 = Car(name='Alexander Graham Bell', color='lex', price=7)


    cars = [u1, u2, u3]

    """Builds sample user/note(s) data"""
    for car in cars:
        try:
            car.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {car.uid}")


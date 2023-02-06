""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Car(db.Model):
    __tablename__ = 'cars'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, unique=True, primary_key=True)
    _brand = db.Column(db.String(255), unique=False, nullable=False)
    _color = db.Column(db.Integer, unique=False, nullable=False)
    _type = db.Column(db.String(255), unique=False, nullable=False)
    _powersource = db.Column(db.String(255), unique=False, nullable=False)
    _price_range = db.Column(db.Integer, unique=False, nullable=False)
   

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, brand, color, type, powersource, price_range):
        self._type = type    # variables with self prefix become part of the object, 
        self._brand = brand
        self._color = color
        self._powersource = powersource
        self._price_range = price_range
        #self.determine_value()

    # gets the brand the car
    @property
    def brand(self):
        return self._brand
    
    # a setter function, allows brand to be updated after initial object creation
    @brand.setter
    def brand(self, brand):
        self._brand = brand

     # gets the color of the car
    @property
    def color(self):
        return self._color
    
    # a setter function, allows color to be updated after initial object creation
    @color.setter
    def color(self, color):
        self._color = color

    # gets the type of the manufacturer or the car
    @property
    def type(self):
        return self._type
    
    # a setter function, allows type to be updated after initial object creation
    @type.setter
    def type(self, type):
        self._type = type
    
    # a powersource getter
    @property
    def powersource(self):
        return self._powersource

    # a setter function to set the car's powersource
    @powersource.setter
    def powersource(self, powersource):
        self._powersource = powersource
    
     # a price getter
    @property
    def price_range(self):
        return self._price_range

    # a setter function to set the car's price_range 
    @price_range.setter
    def price_range(self, price_range):
        self._price_range = price_range
        #self.determine_value() #calls function whenever price_range of car changes 
         
    # @property
    # def value(self):
    #     return self._value
    
    #determines car value based on price_range and stores it by assigning it to object
    def determine_value(self):
        if self._price_range > 60000:
            self._value = "Luxury Car"
        elif self._price_range in range(30000, 60000):
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
            "brand" : self.brand,
            "color" : self.color,
            "type" : self.type,
            "powersource" : self.powersource,
            "price_range" : self.price_range
           # "value" : self.value
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, brand="", color="", powersource="", type="", price_range=""):
        """only updates values with length"""
        if len(brand) > 0:
            self.brand = brand
        if len(color) > 0:
            self.color = color
        if len(type) > 0:
            self.type = type
        if len(powersource) > 0:
            self.powersource = powersource
        self.price_range = price_range
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

    try:
        db.session.query(Car).delete()
        db.session.commit()
    except:
        db.session.rollback()

    """Tester data for table"""
    c1 = Car(brand='Acura', color='gray', powersource='ice', type='suv', price_range='2')
    c2 = Car(brand='Hyundai', color='red', powersource='ice', type='sedan', price_range='1') 
    c3 = Car(brand='Mazda', color='white', powersource='ice', type='sedan', price_range='1')
    c4 = Car(brand='Honda', color='gray', powersource='ice', type='suv', price_range='1')
    c5 = Car(brand='Dodge', color='black', powersource='ice', type='suv', price_range='2')
    c6 = Car(brand='Toyota', color='white', powersource='ice', type='truck', price_range='2') 
    c7 = Car(brand='Hyundai', color='blue', powersource='ice', type='sedan', price_range='1')
    c8 = Car(brand='Chevrolet', color='gray', powersource='ice', type='truck', price_range='2')
    c9 = Car(brand='Jeep', color='gray', powersource='ice', type='suv', price_range='1')
    c10 = Car(brand='Nissan', color='silver', powersource='ice', type='sedan', price_range='1') 
    c11 = Car(brand='Lexus', color='black', powersource='ice', type='sedan', price_range='2')
    c12 = Car(brand='Kia', color='red', powersource='ice', type='suv', price_range='1')
    c13 = Car(brand='Mazda', color='red', powersource='ice', type='truck', price_range='2')
    c14 = Car(brand='Ford', color='white', powersource='ice', type='sedan', price_range='2') 
    c15 = Car(brand='Kia', color='red', powersource='ice', type='truck', price_range='2')
    c16 = Car(brand='Ford', color='gray', powersource='ice', type='suv', price_range='1')
    c17 = Car(brand='Jeep', color='red', powersource='ice', type='truck', price_range='1')
    c18 = Car(brand='Toyota', color='red', powersource='electric', type='suv', price_range='3') 
    c19 = Car(brand='Kia', color='red', powersource='ice', type='truck', price_range='1')
    c20 = Car(brand='Honda', color='white', powersource='ice', type='suv', price_range='1')
    c21 = Car(brand='Hyundai', color='white', powersource='ice', type='sedan', price_range='1')
    c22 = Car(brand='Chevrolet', color='white', powersource='ice', type='suv', price_range='3') 
    c23 = Car(brand='Jeep', color='white', powersource='ice', type='suv', price_range='3')
    c24 = Car(brand='BMW', color='gray', powersource='ice', type='sedan', price_range='4')
    c25 = Car(brand='Ferarri', color='yellow', powersource='ice', type='sports', price_range='4')
    c26 = Car(brand='Tesla', color='red', powersource='electric', type='suv', price_range='4') 
    c27 = Car(brand='Tesla', color='blue', powersource='electric', type='suv', price_range='4')
    c28 = Car(brand='Hummer', color='white', powersource='electric', type='truck', price_range='3')
    c29 = Car(brand='Ford', color='blue', powersource='electric', type='truck', price_range='4')
    c30 = Car(brand='Audi', color='black', powersource='electric', type='suv', price_range='3') 
    c31 = Car(brand='Porsche', color='red', powersource='electric', type='sports', price_range='4')
    c32 = Car(brand='Mercedes', color='silver', powersource='electric', type='sedan', price_range='4')
    c33 = Car(brand='Mazda', color='silver', powersource='electric', type='suv', price_range='2')
    c34 = Car(brand='Nissan', color='blue', powersource='electric', type='suv', price_range='2') 
    c35 = Car(brand='Subaru', color='red', powersource='electric', type='suv', price_range='2')

    cars = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35]

    """Builds sample car/note(s) data"""
    for car in cars:
        try:
            car.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {car.model}")


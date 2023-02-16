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
    _image = db.Column(db.String(255), unique=False, nullable=False)
    _brand = db.Column(db.String(255), unique=False, nullable=False)
    _color = db.Column(db.Integer, unique=False, nullable=False)
    _type = db.Column(db.String(255), unique=False, nullable=False)
    _powersource = db.Column(db.String(255), unique=False, nullable=False)
    _pricerange = db.Column(db.Integer, unique=False, nullable=False)
   

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, image, brand, color, type, powersource, pricerange):
        self._image = image
        self._type = type    # variables with self prefix become part of the object, 
        self._brand = brand
        self._color = color
        self._powersource = powersource
        self._pricerange = pricerange
        #self.determine_value()

    # gets the image url the car
    @property
    def image(self):
        return self._image
    
    # a setter function, allows image url to be updated after initial object creation
    @image.setter
    def image(self, image):
        self._image = image

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
    def pricerange(self):
        return self._pricerange

    # a setter function to set the car's pricerange 
    @pricerange.setter
    def pricerange(self, pricerange):
        self._pricerange = pricerange
        #self.determine_value() #calls function whenever pricerange of car changes 
            
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
            "image": self.image,
            "brand" : self.brand,
            "color" : self.color,
            "type" : self.type,
            "powersource" : self.powersource,
            "pricerange" : self.pricerange
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, image="", brand="", color="", powersource="", type="", pricerange=""):
        """only updates values with length"""
        if len(image) > 0:
            self.image = image
        if len(brand) > 0:
            self.brand = brand
        if len(color) > 0:
            self.color = color
        if len(type) > 0:
            self.type = type
        if len(powersource) > 0:
            self.powersource = powersource
        self.pricerange = pricerange
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
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()

        try:
            db.session.query(Car).delete()
            db.session.commit()
        except:
            db.session.rollback()

        """Tester data for table"""
        c1 = Car(image='1', brand='Acura', color='gray', powersource='ice', type='suv', pricerange='2')
        c2 = Car(image='1', brand='Hyundai', color='red', powersource='ice', type='sedan', pricerange='1') 
        c3 = Car(image='1', brand='Mazda', color='white', powersource='ice', type='sedan', pricerange='1')
        c4 = Car(image='1', brand='Honda', color='gray', powersource='ice', type='suv', pricerange='1')
        c5 = Car(image='1', brand='Dodge', color='black', powersource='ice', type='suv', pricerange='2')
        c6 = Car(image='1', brand='Toyota', color='white', powersource='ice', type='truck', pricerange='2') 
        c7 = Car(image='1', brand='Hyundai', color='blue', powersource='ice', type='sedan', pricerange='1')
        c8 = Car(image='1', brand='Chevrolet', color='gray', powersource='ice', type='truck', pricerange='2')
        c9 = Car(image='1', brand='Jeep', color='gray', powersource='ice', type='suv', pricerange='1')
        c10 = Car(image='1', brand='Nissan', color='silver', powersource='ice', type='sedan', pricerange='1') 
        c11 = Car(image='1', brand='Lexus', color='black', powersource='ice', type='sedan', pricerange='2')
        c12 = Car(image='1', brand='Kia', color='red', powersource='ice', type='suv', pricerange='1')
        c13 = Car(image='1', brand='Mazda', color='red', powersource='ice', type='truck', pricerange='2')
        c14 = Car(image='1', brand='Ford', color='white', powersource='ice', type='sedan', pricerange='2') 
        c15 = Car(image='1', brand='Kia', color='red', powersource='ice', type='truck', pricerange='2')
        c16 = Car(image='1', brand='Ford', color='gray', powersource='ice', type='suv', pricerange='1')
        c17 = Car(image='1', brand='Jeep', color='red', powersource='ice', type='truck', pricerange='1')
        c18 = Car(image='1', brand='Toyota', color='red', powersource='electric', type='suv', pricerange='3') 
        c19 = Car(image='1', brand='Kia', color='red', powersource='ice', type='truck', pricerange='1')
        c20 = Car(image='1', brand='Honda', color='white', powersource='ice', type='suv', pricerange='1')
        c21 = Car(image='1', brand='Hyundai', color='white', powersource='ice', type='sedan', pricerange='1')
        c22 = Car(image='1', brand='Chevrolet', color='white', powersource='ice', type='suv', pricerange='3') 
        c23 = Car(image='1', brand='Jeep', color='white', powersource='ice', type='suv', pricerange='3')
        c24 = Car(image='1', brand='BMW', color='gray', powersource='ice', type='sedan', pricerange='4')
        c25 = Car(image='1', brand='Ferarri', color='yellow', powersource='ice', type='sports', pricerange='4')
        c26 = Car(image='1', brand='Tesla', color='red', powersource='electric', type='suv', pricerange='4') 
        c27 = Car(image='1', brand='Tesla', color='blue', powersource='electric', type='suv', pricerange='4')
        c28 = Car(image='1', brand='Ford', color='white', powersource='electric', type='truck', pricerange='3')
        c29 = Car(image='1', brand='Ford', color='blue', powersource='electric', type='truck', pricerange='4')
        c30 = Car(image='1', brand='Audi', color='black', powersource='electric', type='suv', pricerange='4') 
        c31 = Car(image='1', brand='Porsche', color='red', powersource='electric', type='sports', pricerange='4')
        c32 = Car(image='1', brand='Mercedes', color='silver', powersource='electric', type='sedan', pricerange='4')
        c33 = Car(image='1', brand='Mazda', color='silver', powersource='electric', type='suv', pricerange='2')
        c34 = Car(image='1', brand='Nissan', color='blue', powersource='electric', type='suv', pricerange='2') 
        c35 = Car(image='1', brand='Subaru', color='red', powersource='electric', type='suv', pricerange='2')

        cars = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35]

        """Builds sample car/note(s) data"""
        for car in cars:
            try:
                car.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {car.model}")


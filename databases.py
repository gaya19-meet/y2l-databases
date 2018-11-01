from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_pets(name, age, pet_type, price, num_of_legs, friendly):

  #TODO: complete the functions (you will need to change the function's inputs)
  	pets_object = Product(
  		name=name,
  		age=age,
  		pet_type=pet_type,
  		price=price,
  		num_of_legs=num_of_legs,
  		friendly=friendly)
  	session.add(pets_object)
  	session.commit() 



def update_pets((name, age, pet_type, price, num_of_legs, friendly):
  #TODO: complete the functions (you will need to change the function's inputs)
	pets_object = session.query(id , age) #########33i need to finish 	

def delete_product(id):
  pass

def get_product(id):
  pass

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
	    # TODO: complete this class
	__tablename__ = 'pets'
	id = Column(Integer, primary_key=True)

	name = Column(String)
	age = Column(Integer)
	pet_type = Column(Integer)
	price = Column (Integer)
	num_of_legs = Column(Integer)
	friendly = Column(Boolean)






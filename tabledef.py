from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///thebest.db', echo=True)
Base = declarative_base()

########################################################################
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Artwork(Base):

    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True)
    path = Column(String)
    title = Column(String)
    description = Column(String)
    image = Column(String)

    def __init__(self, path, title, description, image):
        self.path = path
        self.title = title
        self.description = description
        self.image = image

# create tables
Base.metadata.create_all(engine)
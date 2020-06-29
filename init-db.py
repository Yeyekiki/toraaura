import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from getpass import getpass

engine = create_engine('sqlite:///tutorial.db', echo=True)



username = input("Hi! Please choose a username: ")

password1 = getpass("Choose a password: ")
password2 = getpass("Please repeat your password: ")

if password1 is not password2:
    print("Passwords do not match. Please try again")

else:
    
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(username,password)
    session.add(user)

    session.commit()
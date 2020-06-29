import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from getpass import getpass


ARTWORKS = [
    {
        "path": "leon",
        "title": "Leon, Painting",
        "description": "This is a painting of the infamous poster of Luc Besson's masterpiece 'Leon: The Professional'. We can see Leon (Jean Reno) with sunglasses staring at NY's skyline. If you are interested in learning more about or purchasing this piece, please contact me for further information.",
        "image": "leon.jpeg"
    },
    {
        "path": "kanja",
        "title": "Kanja, Picture",
        "description": "This is a picture of Kanja, the second greatest artist in the world (currently).",
        "image": "hippie.jpeg"
    },
    {
        "path": "bath",
        "title": "Bath, Painting",
        "description": "This is a painting inspired by a picture taken by the talented Sarah Babah.",
        "image": "bath.jpeg"
    },
    {
        "path": "hall",
        "title": "Hall, Picture",
        "description": "This is a film picture taken in a cold and isolated hallway that was illuminated by sunlight.",
        "image": "hall.jpeg"
    },
]
engine = create_engine('sqlite:///thebest.db', echo=True)

username = input("Hi! Please choose a username: ")

password1 = getpass("Choose a password: ")
password2 = getpass("Please repeat your password: ")

if password1 == password2:
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(username,password1)
    session.add(user)

    for artwork in ARTWORKS:
        piece = Artwork(artwork["path"], artwork["title"], artwork["description"], artwork["image"])
        session.add(piece)

    session.commit()   

else:
    print("Passwords do not match. Please try again")

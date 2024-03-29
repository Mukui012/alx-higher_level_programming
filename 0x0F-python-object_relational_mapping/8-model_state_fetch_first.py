#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    """ create engine from database """
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    my_instance = session.query(State).order_by(State.id).first()
    if my_instance:
        print("{:d}: {:s}".format(my_instance.id, my_instance.name))
    else:
        print("Nothing")

    session.close()

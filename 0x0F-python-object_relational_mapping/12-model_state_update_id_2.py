#!/usr/bin/python3
"""
Script that changes the name of a State object from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ Create engine for the database """
    username = argv[1]
    password = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Updates name of state """
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    session.commit()
    session.close()

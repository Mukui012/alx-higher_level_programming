#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
	""" Acces the database """
	username = argv[1]
	password = argv[2]
	db = argv[3]
	engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
			format(username, password, db), pool_pre_ping=True)
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	session = Session()

	""" Add new state """
	new_state = State(name="Louisiana")
	session.add(new_state)
	session.commit()

	print("{:d}".format(new.id))
	
	session.close()

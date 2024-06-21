#!/usr/bin/python3
"""
Write a script that deletes all State objects
with a name containing the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_delete = session.query(State).filter(State.name.like('%a%')).all()

    for states in state_delete:
        session.delete(states)

    session.commit()

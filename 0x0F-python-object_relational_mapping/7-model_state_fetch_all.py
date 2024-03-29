#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__== "__main__":
    engine = create_engine('mysql+msqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    for instance in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
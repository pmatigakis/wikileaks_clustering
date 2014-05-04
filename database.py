from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_session(database, username, password):
    engine = create_engine("postgresql+psycopg2://%s:%s@localhost/%s" % (username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    return session


from sqlalchemy import create_engine

def get_engine(db_url='sqlite:///gifty.db'):
    """
    Creates and returns a SQLAlchemy engine connected to the specified database URL.

    :param db_url: Database URL. Defaults to an SQLite file database named 'gifty.db'.
    :return: SQLAlchemy Engine
    """
    engine = create_engine(db_url, echo=False, future=True)
    return engine

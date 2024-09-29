from .engine import get_engine
from models.base import Base
from models import Giftee, Gift, Event, Photo

def initialize_database():
    """
    Initializes the database by creating all the defined tables.
    """
    engine = get_engine()
    # Create all tables in the database
    Base.metadata.create_all(engine)
    print("Database initialized with all tables.")

if __name__ == '__main__':
    initialize_database()

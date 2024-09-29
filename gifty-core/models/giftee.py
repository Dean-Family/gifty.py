from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

# This model is designed to ensure data durability and prevent unintended loss of records across the Giftee, Gift, and Event tables.
class Giftee(Base):
    __tablename__ = 'giftees'

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)

    # Relationship to gifts
    gifts = relationship('Gift', back_populates='giftee', cascade='save-update, merge')

    def __init__(self, firstname=None, lastname=None):
        self.firstname = firstname
        self.lastname = lastname

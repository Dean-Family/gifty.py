from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .base import Base

# Uniqueness constraints are intentionally avoided to allow flexibility.
class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    event_description = Column(String, nullable=True)
    date = Column(Date, nullable=True)
    recurring = Column(String, default='None')

    # Relationship to gifts
    gifts = relationship('Gift', back_populates='event', cascade='save-update, merge')

    def __init__(self, name=None, event_description=None, date=None, recurring=None):
        self.name = name
        self.event_description = event_description
        self.date = date
        self.recurring = recurring

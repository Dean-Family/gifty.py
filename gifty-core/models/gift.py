from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import BLOB
from .base import Base

# Foreign keys are set with `ondelete='SET NULL'`, so if a Giftee or Event is deleted, associated gifts are preserved.
class Gift(Base):
    __tablename__ = 'gifts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    cents = Column(Integer, nullable=True)
    item_description = Column(String, nullable=True)
    link = Column(String, nullable=True)
    location = Column(String, nullable=True)
    status = Column(String, nullable=True)

    giftee_id = Column(Integer, ForeignKey('giftees.id', ondelete='SET NULL'), nullable=True)
    event_id = Column(Integer, ForeignKey('events.id', ondelete='SET NULL'), nullable=True)

    # Relationships
    giftee = relationship('Giftee', back_populates='gifts')
    event = relationship('Event', back_populates='gifts')
    photos = relationship('Photo', back_populates='gift', cascade='save-update, merge')

    def __init__(self, name=None, cents=0, item_description=None, link=None, location=None, status=None, giftee=None, event=None):
        self.name = name
        self.cents = cents
        self.item_description = item_description
        self.link = link
        self.location = location
        self.status = status
        self.giftee = giftee
        self.event = event

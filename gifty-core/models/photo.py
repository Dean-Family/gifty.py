from sqlalchemy import Column, Integer, String, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from .base import Base

# Photos are linked to a specific gift through a ForeignKey relationship.
class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    image_data = Column(BLOB, nullable=False)  # Binary image data
    description = Column(String, nullable=True)

    # Foreign key to the gift
    gift_id = Column(Integer, ForeignKey('gifts.id', ondelete='CASCADE'), nullable=False)

    # Relationship to gift
    gift = relationship('Gift', back_populates='photos')

    def __init__(self, image_data=None, description=None, gift=None):
        self.image_data = image_data
        self.description = description
        self.gift = gift

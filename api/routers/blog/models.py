from api.database import Base
from sqlalchemy import Column, Integer, String


class BlogModel(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)

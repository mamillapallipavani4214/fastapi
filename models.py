from sqlalchemy import Column, Integer, String
from database import Base

class mobile(Base):
    __tablename__ = "mobiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location= Column(String(50),nullable=False)
    department=Column(String(50),nullable=False)
    email=Column(String(50),nullable=False)

    

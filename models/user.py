from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):

    __tablename__ = "users"

    # attributes : 

    id = Column(Integer, primary_key=True, index=True)

    age = Column(Integer , nullable=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    hashed_passwd = Column(String , nullable = False )

    # relationships : 
    requests = relationship("Request" , back_populates="user")
    medical_reports = relationship("MedicalReport" , back_populates="user")

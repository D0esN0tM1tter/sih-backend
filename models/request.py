from sqlalchemy import Column , Integer, ForeignKey, String, DateTime, Enum
from app.db.database import Base
from sqlalchemy.orm import relationship
import enum
import datetime



class LLMType(str , enum.Enum) : 

    local = "local" 

    api = "api"


class Request(Base) : 

    __tablename__ = "requests" 

    id = Column(Integer , primary_key=True,nullable=False , index=True ) 

    user_id = Column(Integer, ForeignKey("users.id") , nullable=False)

    prompt =  Column(String , nullable=False) 

    response = Column(String , nullable=False) 

    llm_type = Column(Enum(LLMType) , nullable=False)

    timestamp = Column(DateTime , nullable=False) 

    # relationships : 
    user = relationship("User" , back_populates="requests") 

    
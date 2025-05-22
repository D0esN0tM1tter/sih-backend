from sqlalchemy import Column, Integer, ForeignKey, Text, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class MedicalReport(Base):

    __tablename__ = "medical_reports"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    filename = Column(String, nullable=False)

    parsed_text = Column(Text, nullable=True)

    image_paths = Column(Text, nullable=True)  

    user = relationship("User", back_populates="medical_reports")

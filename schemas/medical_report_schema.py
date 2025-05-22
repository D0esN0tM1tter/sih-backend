# app/schemas/medical_report_schema.py
from pydantic import BaseModel
from typing import Optional

class MedicalReportBase(BaseModel):
    filename: str
    parsed_text: Optional[str] = None
    image_paths: Optional[str] = None

class MedicalReportCreate(MedicalReportBase):
    user_id: int

class MedicalReportSchema(MedicalReportBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

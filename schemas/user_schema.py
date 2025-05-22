# app/schemas/user_schema.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.schemas.request_schema import RequestSchema
from app.schemas.medical_report_schema import MedicalReportSchema

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

class UserCreate(UserBase):
    password: str  # plain password for creation only

class UserSchema(UserBase):
    id: int
    requests: List[RequestSchema] = []
    medical_reports: List[MedicalReportSchema] = []

    class Config:
        orm_mode = True

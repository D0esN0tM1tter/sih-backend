# app/schemas/request_schema.py
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class LLMType(str, Enum):
    local = "local"
    api = "api"

class RequestBase(BaseModel):
    prompt: str
    response: str
    llm_type: LLMType
    timestamp: datetime

class RequestCreate(RequestBase):
    user_id: int

class RequestSchema(RequestBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

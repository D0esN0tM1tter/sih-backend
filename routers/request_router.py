# app/routers/request_router.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.request_repository import RequestRepository
from app.services.request_services import RequestService
from app.schemas.request_schema import RequestCreate, RequestSchema

router = APIRouter(prefix="/requests", tags=["Requests"])

def get_request_service(db: Session = Depends(get_db)) -> RequestService:
    repo = RequestRepository(db)
    return RequestService(repo)

@router.post("/", response_model=RequestSchema)
def create_request(
    request_create: RequestCreate,
    service: RequestService = Depends(get_request_service)
):
    return service.create_request(request_create)

@router.get("/{request_id}", response_model=RequestSchema)
def get_request_by_id(
    request_id: int,
    service: RequestService = Depends(get_request_service)
):
    request = service.get_by_id(request_id)
    if not request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    return request

@router.get("/", response_model=list[RequestSchema])
def get_all_requests(
    service: RequestService = Depends(get_request_service)
):
    return service.get_all()

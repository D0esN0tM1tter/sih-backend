# app/routers/medical_report_router.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.medical_report_repository import MedicalReportRepository
from app.services.medical_report_services import MedicalReportService
from app.schemas.medical_report_schema import MedicalReportCreate, MedicalReportSchema

router = APIRouter(prefix="/medical-reports", tags=["Medical Reports"])

def get_medical_report_service(db: Session = Depends(get_db)) -> MedicalReportService:
    repo = MedicalReportRepository(db)
    return MedicalReportService(repo)

@router.post("/", response_model=MedicalReportSchema)
def create_medical_report(
    report_create: MedicalReportCreate,
    service: MedicalReportService = Depends(get_medical_report_service)
):
    return service.create_medical_report(report_create)

@router.get("/{report_id}", response_model=MedicalReportSchema)
def get_medical_report_by_id(
    report_id: int,
    service: MedicalReportService = Depends(get_medical_report_service)
):
    report = service.get_by_id(report_id)
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medical report not found")
    return report

@router.get("/", response_model=list[MedicalReportSchema])
def get_all_medical_reports(
    service: MedicalReportService = Depends(get_medical_report_service)
):
    return service.get_all()

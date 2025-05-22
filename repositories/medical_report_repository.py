from sqlalchemy.orm import Session
from app.models.medical_report import MedicalReport

class MedicalReportRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, report: MedicalReport):
        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)
        return report

    def find_by_id(self, report_id: int):
        return self.db.query(MedicalReport).filter(MedicalReport.id == report_id).first()

    def find_by_user(self, user_id: int):
        return self.db.query(MedicalReport).filter(MedicalReport.user_id == user_id).all()

    def find_all(self):
        return self.db.query(MedicalReport).all()

    def delete(self, report: MedicalReport):
        self.db.delete(report)
        self.db.commit()

from app.repositories.medical_report_repository import MedicalReportRepository
from app.models.medical_report import MedicalReport

class MedicalReportService:
    def __init__(self, repo: MedicalReportRepository):
        self.repo = repo

    def create(self, user_id: int, filename: str, parsed_text: str = "", image_paths: str = "") -> MedicalReport:
        report = MedicalReport(
            user_id=user_id,
            filename=filename,
            parsed_text=parsed_text,
            image_paths=image_paths
        )
        return self.repo.create(report)

    def find_by_id( self ,id : int) : 
        return self.repo.find_by_id(id)

    def find_all(self) : 
        return self.repo.find_all()
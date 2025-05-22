from sqlalchemy.orm import Session
from app.models.request import Request

class RequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, request: Request):
        self.db.add(request)
        self.db.commit()
        self.db.refresh(request)
        return request

    def find_by_id(self, request_id: int):
        return self.db.query(Request).filter(Request.id == request_id).first()

    def find_by_user(self, user_id: int):
        return self.db.query(Request).filter(Request.user_id == user_id).all()

    def find_all(self):
        return self.db.query(Request).all()

    def delete(self, request: Request):
        self.db.delete(request)
        self.db.commit()

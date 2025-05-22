from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def find_by_id (self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def find_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def find_all(self):
        return self.db.query(User).all()

    def delete(self, user: User):
        self.db.delete(user)
        self.db.commit()

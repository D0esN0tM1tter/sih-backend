from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, instance):
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, model, id_):
        return self.db.query(model).filter(model.id == id_).first()

    def list(self, model):
        return self.db.query(model).all()

    def delete(self, instance):
        self.db.delete(instance)
        self.db.commit()

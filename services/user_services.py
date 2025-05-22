from app.repositories.user_repository import UserRepository
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def create(self, name: str, email: str, password: str, age: int) -> User:
        hashed_password = self.hash_password(password)
        user = User(name=name, email=email, hashed_passwd=hashed_password, age=age)
        return self.user_repository.create(user)

    def authenticate(self, email: str, password: str) -> User | None:
        user = self.user_repository.find_by_email(email)
        if user and self.verify_password(password, user.hashed_passwd):
            return user
        return None

    def find_by_email(self, email: str) -> User | None:
        return self.user_repository.find_by_email(email)

    def find_by_id(self, user_id: int) -> User | None:
        return self.user_repository.find_by_id(user_id)

    def find_all(self) -> list[User]:
        return self.user_repository.find_all()

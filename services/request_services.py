from app.repositories.request_repository import RequestRepository
from app.models.request import Request, LLMType
import datetime

class RequestService:
    
    def __init__(self, request_repository: RequestRepository):
        self.request_repository = request_repository

    def create_request(self, user_id: int, prompt: str, response: str, llm_type: LLMType) -> Request:

        req = Request(
            user_id=user_id,
            prompt=prompt,
            response=response,
            llm_type=llm_type,
            timestamp=datetime.datetime.utcnow()
        )
        return self.request_repository.create(req)
    
    def find_all_requests(self) : 
        return self.request_repository.list()
    
    def find_by_id(self , id : int) : 
        return self.request_repository.find_by_id(id)

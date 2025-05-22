from fastapi import APIRouter
from app.schemas.request_schema import RequestBase
from app.services.llm_service import LLMService 
from app.services.gemini_service import GeminiService


llm_router = APIRouter() 

# Instanciating the 
local_llm = LLMService() 
gemini = GeminiService()



@llm_router.post("/local-llm" , re) 
def generate(input : RequestBase) :  
    # extract the prompt from the request model :
    prompt = input.prompt
    result = local_llm.generate(prompt) 







from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import user_router, request_router, medical_report_router

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(request_router.router, prefix="/requests", tags=["requests"])
app.include_router(medical_report_router.router, prefix="/medical-reports", tags=["medical_reports"])

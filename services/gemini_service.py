import google.generativeai as genai
from PIL import Image
from fastapi import UploadFile
import os
import json
from dotenv import load_dotenv
from app.services.pdf_parser import parse_pdf_file
from app.schemas.medical_report_schema import MedicalReportCreate

load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

class GeminiService:
    def __init__(self):
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel(MODEL)

    def generate(self, uploaded_file: UploadFile, user_id: int , prompt : str) -> str:
        # Step 1: Parse PDF into MedicalReportCreate
        report: MedicalReportCreate = parse_pdf_file(uploaded_file, user_id)

        # Step 2: Extract text and image paths
        text_content = report.parsed_text or ""
        image_paths = json.loads(report.image_paths or "[]")

        # Step 3: Load images into PIL format
        images = []
        for path in image_paths:
            try:
                img = Image.open(path)
                images.append(img)
            except Exception as e:
                print(f"Could not open image {path}: {e}")

        # Step 4: Compose multimodal input for Gemini
        input = f"{prompt} + "f"You are a healthcare expert. Please analyze the following medical report:\n{text_content}"
        input_data = [input] + images

        # Step 5: Call Gemini and return the result
        try:
            response = self.model.generate_content(input_data)
            return response.text
        except Exception as e:
            print(f"Gemini generation failed: {e}")
            raise

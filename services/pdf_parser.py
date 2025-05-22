from fastapi import UploadFile
import fitz
import os
import uuid
import json
from pathlib import Path
from app.schemas.medical_report_schema import MedicalReportCreate

UPLOAD_DIR = Path("uploads/reports")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def parse_pdf_file(uploaded_file: UploadFile, user_id: int) -> MedicalReportCreate:
    # Save uploaded file to disk temporarily
    temp_filename = f"{uuid.uuid4()}_{uploaded_file.filename}"
    temp_path = UPLOAD_DIR / temp_filename

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.file.read())

    doc = fitz.open(temp_path)
    text_content = []
    image_paths = []

    for page in doc:
        text_content.append(page.get_text())

        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]

            image_filename = f"{uuid.uuid4()}.{ext}"
            image_path = UPLOAD_DIR / image_filename

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(str(image_path))

    doc.close()

    return MedicalReportCreate(
        filename=uploaded_file.filename,
        parsed_text="\n".join(text_content),
        image_paths=json.dumps(image_paths),
        user_id=user_id
    )

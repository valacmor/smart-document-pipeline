import os
import shutil
import logging
from fastapi import FastAPI, UploadFile, File
from main import process_receipt_pipeline

logger = logging.getLogger(__name__)

app = FastAPI(title="Smart document API")

@app.get("/")
def health_check():
    return{"status": "ok", "message": "Server is on!"}

@app.post("/upload_receipt/")
def upload_receipt(file: UploadFile = File(...)):
    temp_file_path = f"temp_{file.filename}"

    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result_data = process_receipt_pipeline(temp_file_path)
        return{
            "status": "success",
            "filename": file.filename,
            "parsed_data": result_data
        }
    except Exception as e:
        logger.exception(f"Unexpected error during post process with file {file.filename}")
        return{
            "status": "fail",
            "filename": file.filename,
            "parsed_data": None
        }

    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)



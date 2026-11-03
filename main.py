from src.ocr import OCRProcessor
from src.parser import parse_receipt_data
from src.database import DatabaseHandler

ocr = None
db_handler = None

def process_receipt_pipeline(image_path: str):    
    global ocr, db_handler
    
    if ocr is None:
        ocr = OCRProcessor()
    if db_handler is None:
        db_handler = DatabaseHandler()

    extracted_text = ocr.extract_text(image_path)

    if not extracted_text:
        print("Error: Can't extract text from file")
        return

    data = parse_receipt_data(extracted_text)
    
    db_handler.save_document(data)
    print("Successfully saved!")

    return data

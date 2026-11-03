from src.ocr import OCRProcessor
from src.parser import parse_receipt_data
from src.database import DatabaseHandler

ocr = OCRProcessor()
db_handler = DatabaseHandler()

def process_receipt_pipeline(image_path: str):    
    extracted_text = ocr.extract_text(image_path)

    if not extracted_text:
        print("Error: Can't extract text from file")
        return

    data = parse_receipt_data(extracted_text)
    
    db_handler.save_document(data)
    print("Successfuly saved!")

    return data

if __name__ == "__main__":
    test_image = r"D:\sample.jpg"
    
    process_receipt_pipeline(test_image)
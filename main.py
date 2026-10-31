import os
from src.ocr import OCRProcessor
from src.parser import parse_receipt_data
from src.database import DatabaseHandler

ocr = OCRProcessor()
db_handler = DatabaseHandler()

def process_receipt_pipeline(image_path: str):    
    print(f"\n=== Запуск пайплайна для файла: {image_path} ===")

    extracted_text = ocr.extract_text(image_path)

    if not extracted_text:
        print("Остановка: Не удалось извлечь текст из файла.")
        return

    data = parse_receipt_data(extracted_text)
    print(f"Вытащенные данные: {data}")

    db_handler.save_document(data)
    print("Успех: Данные сохранены в Базу Данных!")

if __name__ == "__main__":
    test_image = r"D:\sample.jpg"
    
    process_receipt_pipeline(test_image)
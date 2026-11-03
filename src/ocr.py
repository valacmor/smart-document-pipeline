import easyocr
import os
import logging

logger = logging.getLogger(__name__)

class OCRProcessor:
    def __init__(self, language=None):
        if language is None:
            language = ['ru','en']

        print("loading model in memory...")
        self.reader = easyocr.Reader(language)

    def extract_text(self, image_path: str) -> list:
        try:    
            if os.path.exists(image_path):
                return self.reader.readtext(image_path, detail=0)
                
            else:
                logger.warning(f"Error: File {image_path} is not found!")
                return[] 
        except Exception as e:
            logger.exception(f"Unexpected error during OCR processing for {image_path}")
            return []


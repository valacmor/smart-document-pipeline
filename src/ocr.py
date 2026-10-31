import easyocr
import os

class OCRProcessor:
    def __init__(self, language=None):
        if language is None:
            language = ['ru','en']

        print("loading model in memory...")
        self.reader = easyocr.Reader(language)

    def extract_text(self, image_path: str) -> list:
        if os.path.exists(image_path):
            return self.reader.readtext(image_path, detail=0)
            
        else:
            print(f"Error: File {image_path} is not found!")
            return[] #return nothing if file is not found

if __name__ == "__main__":
    ocr = OCRProcessor()

    test_image = r"D:\sample.jpg" 

    result = ocr.extract_text(test_image)
    print(f"OCR work result: {result}")   
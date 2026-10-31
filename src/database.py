import sqlite3
from datetime import datetime

class DatabaseHandler:
    def __init__(self, db_name="documents.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()  
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at,
                company TEXT,
                inn TEXT,
                total FLOAT,
                date TEXT)
            ''')

    def save_document(self, data: dict):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()  
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute(
                "INSERT INTO documents (company, inn, total, date) VALUES (?, ?, ?, ?, ?)",
                (created_at, data["company"], data["inn"], data["total"], data["date"])
            )

if __name__ == "__main__":
    db = DatabaseHandler()
    
    sample_data = {
        "company": "ООО ВЕКТОР",
        "inn": "771234567890",
        "total": 350.00,
        "date": "12.05.2024"
    }
    
    db.save_document(sample_data)
    print("Данные успешно сохранены в БД!")    
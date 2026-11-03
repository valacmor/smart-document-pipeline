# Smart Document OCR Pipeline
Автоматизированный микросервис для распознавания кассовых чеков (можно подвести и в документе). Проект использует компьютерное зрение (OCR) для извлечения текста из изображений, структурирует ключевые данные (ИНН, Суммы, Даты) с помощью алгоритмов парсинга и сохраняет результаты в SQL базу данных.

## Стек
- **Language:** Python 3.10+
- **ML / Computer Vision:** EasyOCR, PyTorch
- **API Framework:** FastAPI, Uvicorn
- **Database:** SQLite3
- **Data Processing:** Regular Expressions (Regex)

## Архитектура системы

```text
 [ Изображение чека (.jpg/.png) ]
                ↓
   1. OCR Module (src/ocr.py)         <<< Извлечение сырого текста (EasyOCR)
                ↓
   2. Parser Module (src/parser.py)  <<< Извлечение ИНН, Даты и Итого (Regex)
                ↓
   3. DB Handler (src/database.py)   <<< Сохранение карточки в SQLite (Context Manager)
                ↓
   4. REST API (app.py)              <<< Выдача JSON ответа через FastAPI

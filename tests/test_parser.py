from src.parser import parse_receipt_data

def test_parse_valid_receipt():
    raw_lines = [
        "ООО Пример",
        "ИНН 771234567890",
        "ИТОГО 350.00",
        "15.11.2026"
    ]
    result = parse_receipt_data(raw_lines)

    assert result["company"] == "ООО Пример"
    assert result["inn"] == "771234567890"
    assert result["total"] == 350.0
    assert result["date"] == "15.11.2026"

def test_parse_missing_inn():
    raw_lines = [
        "Кассовый чек",
        "Итого 350.00"
    ]
    result = parse_receipt_data(raw_lines)

    assert result["inn"] == None
    assert result["total"] == 350.0

def test_parse_comma_in_total():
    raw_lines = ["ИТОГО 350,0"]

    result = parse_receipt_data(raw_lines)
    assert result["total"] == 350.0
import re

def parse_receipt_data(ocr_lines: list):
    decoded_data = {
        "company": "-",
        "inn": "-",
        "total": "0.0",
        "date": "01.01.0001"
    }

    for i in range(len(ocr_lines)):
        ocr_line = ocr_lines[i]
        if 'ИНН' in ocr_line:
            inn_match = re.search(r'\d{10,12}', ocr_line)
            if inn_match:
                decoded_data["inn"] = inn_match.group()
                if ocr_line > 0:
                    decoded_data["company"] = ocr_lines[i - 1]

        if 'итого' in ocr_line.lower(): 
            total_match = re.search(r'\d+[.,]\d{2}', ocr_line)
            if total_match:
                raw_total = total_match.group()
                clean_total = raw_total.replace(',','.')
                try:
                    decoded_data["total"] = float(clean_total)
                except ValueError:
                    print(f"Не удалось перевести в число: {clean_total}")
                    decoded_data["total"] = 0.0

                    

        date_match = re.search(r'\d{2}[-./]\d{2}[-./]\d{2,4}', ocr_line)
        if date_match:
            decoded_data["date"] = date_match.group()

    return(decoded_data)
        
                
            


import os
import uuid
import pdf2image
import pytesseract
from pytesseract import Output, TesseractError
from PyPDF2 import PdfReader
from configs.settings import RAW_DATA_PATH, PROCESSED_DATA_PATH


def parse_pdf(file_path: str) -> str:
    document_id = str(uuid.uuid4())
    processed_dir = os.path.join(PROCESSED_DATA_PATH, document_id)
    os.makedirs(processed_dir, exist_ok=True)

    full_text = []
    reader = PdfReader(file_path)

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if not text.strip():
            images = pdf2image.convert_from_path(file_path, first_page=page_number, last_page=page_number)
            ocr_text = pytesseract.image_to_string(images[0], lang='rus+eng')
            text = ocr_text.strip()

        with open(os.path.join(processed_dir, f"page_{page_number}.txt"), "w", encoding="utf-8") as file:
            file.write(text)

        full_text.append(text)

    with open(os.path.join(processed_dir, "full_text.txt"), "w", encoding="utf-8") as file:
        file.write("\n".join(full_text))

    return document_id

def process_raw_document(file_name: str):
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    if not os.path.exists(file_path):
        print(f"Ошибка: файл {file_path} не найден.")
        return
    try:
        document_id = parse_pdf(file_path)
        print(f"Документ обработан. ID: {document_id}")
    except Exception as e:
        print(f"Ошибка обработки документа: {e}")


if __name__ == "__main__":
    process_raw_document("1.pdf")

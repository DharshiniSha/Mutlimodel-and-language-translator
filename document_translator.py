import os
from deep_translator import GoogleTranslator
from docx import Document
import PyPDF2

def translate_document(file_path, target_lang):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    elif ext == ".docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    elif ext == ".pdf":
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    else:
        raise ValueError("Unsupported file format!")

    translated_text = GoogleTranslator(source="auto", target=target_lang).translate(text)

    output_file = f"translated_document_{target_lang}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translated_text)

    return translated_text, os.path.abspath(output_file)

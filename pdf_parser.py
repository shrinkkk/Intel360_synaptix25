import fitz  # PyMuPDF
import pdfplumber
import os

def is_table(text):
    """Basic check to determine if extracted text resembles a table."""
    lines = text.split("\n")
    structured_lines = [line for line in lines if " " in line or "|" in line]
    return len(structured_lines) > len(lines) * 0.5  # If most lines look structured

def extract_text(file_path):
    """Extract text from PDF and determine if it's a table."""
    with fitz.open(file_path) as doc:
        text = "\n".join([page.get_text("text") for page in doc])
    
    if is_table(text):
        return extract_table(file_path)
    return text

def extract_table(file_path):
    """Extract tables from PDF using pdfplumber."""
    table_data = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    table_data.append(" | ".join([cell if cell else "" for cell in row]))
    return "\n".join(table_data) if table_data else "No table detected."

if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Change this to test different PDFs
    if os.path.exists(pdf_path):
        print(extract_text(pdf_path))
    else:
        print("File not found.")
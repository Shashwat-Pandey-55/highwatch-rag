# processing/parser.py
import io
import PyPDF2

def extract_text(content: bytes, mime_type: str, file_name: str) -> str:
    if mime_type == 'application/pdf':
        return extract_pdf_text(content)
    elif mime_type in ['text/plain', 'application/vnd.google-apps.document']:
        return content.decode('utf-8', errors='ignore')
    else:
        print(f'Unsupported type: {mime_type}')
        return ''

def extract_pdf_text(content: bytes) -> str:
    reader = PyPDF2.PdfReader(io.BytesIO(content))
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text.strip()

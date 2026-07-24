from .loader import load_pdf
from .cleaner import clean_text
from .generator import generate_markdown
from .saver import save_document
from .parser import parse_response
from pathlib import Path

pdf_path = Path(__file__).parent / "rbi_guideline.pdf"

text = load_pdf(pdf_path)

clean = clean_text(text)

response = generate_markdown(clean)
print(response)
data = parse_response(response)


save_document(data)

print("Knowledge Added Successfully")
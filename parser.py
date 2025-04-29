import re
import pdfplumber  # pip install pdfplumber
from constants import * 

def extract_numbers_from_pdf(path):
    numbers = []
    # matches optional minus, digits with optional groups of ,###, optional decimal part
    number_pattern = re.compile(r'-?\d{1,3}(?:,\d{3})*(?:\.\d+)?')
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            for match in number_pattern.findall(text):
                clean = match.replace(',', '')
                if '.' in clean:
                    numbers.append(float(clean))
                else:
                    numbers.append(int(clean))
    return numbers


def extract_dollar_values(txt_path = DEFAULT_TXT_FILE_PATH, allow_duplicates = True):
    # matches $ followed by 1–3 digits, optional groups of ,###, optional .decimal
    pattern = re.compile(r'\$\d{1,3}(?:,\d{3})*(?:\.\d+)?')
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()
    matches = pattern.findall(text)
    if allow_duplicates:
        values = [float(m.replace('$','').replace(',','')) for m in matches]
    else:
        values = list(set([float(m.replace('$','').replace(',','')) for m in matches]))
    return values


if __name__ == "__main__":
    nums = extract_dollar_values("data.txt")
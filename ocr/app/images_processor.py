from PIL import Image

import pytesseract

def replace_jump_lines(string):
    return string.replace("\n", "")

def process_image(file_name) -> str:
    # Simple image to string
    string = pytesseract.image_to_string(Image.open(file_name))
    return replace_jump_lines(string)
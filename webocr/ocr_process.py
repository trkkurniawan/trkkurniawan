try:  
    from PIL import Image
except ImportError:  
    import Image

from pytesseract2 import image_to_string


def ocr_core(filename):  
    ## OCR process
    text = image_to_string(Image.open(filename)) 
    return text
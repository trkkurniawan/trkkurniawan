from pytesseract2 import image_to_string
from PIL import Image
file = "./static/uploads/sample.png"

def ocr_core(filename):  
    ## OCR process
    text = image_to_string(Image.open(filename)) 
    return text

if __name__ == '__main__':  
    tes = ocr_core(file)
    print(tes)
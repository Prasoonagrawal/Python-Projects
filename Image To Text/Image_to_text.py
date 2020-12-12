import pytesseract
import os
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r"D:\python package\tesseract.exe"
def convert():
    location=input("Enter image name with location: ")
    img=Image.open(location)
    text=pytesseract.image_to_string(img)
    print(text)

convert()

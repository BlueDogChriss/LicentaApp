import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Cristi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image

#img1=Image.open('photo.jpg')
img=Image.open('factura-fiscala.jpg')

text = tess.image_to_string(img)
#text1= tess.image_to_string(img1)

print(text)
#print(text1)

#vue - front (prototype) + express and seq 
#api media for pictures
#photo->server->extractText->machingProduse
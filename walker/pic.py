import pytesseract
import requests as req
from PIL import Image
from io import BytesIO

def parseNumber(url):
    response = req.get(url)
    img = Image.open(BytesIO(response.content))
    return pytesseract.image_to_string(img, lang="eng", config="-psm 6")


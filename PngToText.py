import pytesseract as pt
from PIL import Image
path=r'D:\tess\tesseract.exe'
pt.pytesseract.tesseract_cmd=path
img=Image.open('imgs/images_0.png')
text=pt.image_to_string(img,lang='chi_sim')
print(text)
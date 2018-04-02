from PIL import Image
import pytesseract
#依赖于tesseract.exe图像识别解析器,下载
#C:\Python34\Lib\site-packages\pytesseract\tesseract.py   文件中修改如下:
#tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


image_temp = Image.open('test.png')
signin_code = pytesseract.image_to_string(image_temp,lang='eng')
print(signin_code)
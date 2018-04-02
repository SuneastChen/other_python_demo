
from PIL import ImageGrab,Image
import pytesseract

# import image
# except ImportError:
#     from PIL import 

def yz_code():
    # bbox = (1348, 423, 1455, 455)  # 截图范围，这个取决你验证码的位置
    # img = ImageGrab.grab(bbox=bbox)
    # img.save("D:\\py\\login\\image_code.jpg")   # 设置路径
    # img.show()

    img = Image.open('igg.bmp')  # PIL库加载图片
    # print img.format, img.size, img.mode  # 打印图片信息
    img = img.convert('RGBA')  # 转换为RGBA
    pixdata = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)

    img.save("igg1.bmp")  # 由于tesseract限制，这里必须存到本地文件

    image_temp = Image.open('igg1.bmp')

    signin_code = pytesseract.image_to_string(image_temp,lang='eng')
    
    print(signin_code)

yz_code()
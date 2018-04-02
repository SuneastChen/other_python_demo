from PIL import ImageGrab,Image
import pytesseract


def yz_code():
    # bbox = (1348, 423, 1455, 455)  # 截图范围，这个取决你验证码的位置
    # img = ImageGrab.grab(bbox=bbox)
    # img.save("D:\\py\\login\\image_code.jpg")   # 设置路径
    # img.show()

    img = Image.open('img5.bmp')  # PIL库加载图片
    # print img.format, img.size, img.mode  # 打印图片信息
    img = img.convert('RGBA')  # 转换为RGBA
    pix = img.load()  # 读取为像素
    for x in range(img.size[0]):  # 处理上下黑边框
        pix[x, 0] = pix[x, img.size[1] - 1] = (255, 255, 255, 255)
    for y in range(img.size[1]):  # 处理左右黑边框
        pix[0, y] = pix[img.size[0] - 1, y] = (255, 255, 255, 255)
    for y in range(img.size[1]):  # 二值化处理，这个阈值为R=95，G=95，B=95
        for x in range(img.size[0]):
            if pix[x, y][0] < 95 or pix[x, y][1] < 95 or pix[x, y][2] < 95:
                pix[x, y] = (0, 0, 0, 255)
            else:
                pix[x, y] = (255, 255, 255, 255)

    img.save("img5.png")  # 由于tesseract限制，这里必须存到本地文件

    image_temp = Image.open('img5.png')

    signin_code = pytesseract.image_to_string(image_temp,lang='eng')
    
    print(signin_code)

yz_code()







import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter
#Image 负责处理图片
#ImageDraw 负责处理画笔
#ImageFont 负责处理字体
#ImageFilter 负责处理滤镜


#项目思路
    #1.定义一张图片
img=Image.new('RGB',(150,50),(255,255,255))
#'RGB'颜色模式,图片大小,具体的颜色值

    #2.创建画笔
draw=ImageDraw.Draw(img)

    #3.绘制线条和点
        #绘制线条,两个点决定一条线
for i in range(random.randint(1,10)):
    draw.line([(random.randint(1,150),random.randint(1,150)),
               (random.randint(1,150),random.randint(1,150))],
              fill=(0,0,0))
        #给制点
    for i in range(200):
        draw.point([random.randint(1,150),random.randint(1,150)],
                   fill=(0,0,0))

    #4.绘制我们的文字
font_list=list('abcdefghigkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ23456789')
c_chars=''.join(random.sample(font_list,5))
#random.sample(font_list,5)在样本中随机取出5个元素
font=ImageFont.truetype('simsun.ttc',40)   #设定字体及大小
draw.text((5,5),c_chars,font=font,fill='green')
# 参数:文字的位置,距离上和左的距离;文字内容;字体;字体颜色
    #5.定义扭曲的参数
params=[1-float(random.randint(1,2)/100),
        0,
        0,
        0,
        1-float(random.randint(1,2)/100),
        float(random.randint(1,2))/500,
        0.001,
        float(random.randint(1,1))/500
        ]
    #6.滤镜
        #添加滤镜
img=img.transform((150,50),Image.PERSPECTIVE,params)
#参数:扭曲的范围;扭曲的样式,扭曲的参数
        #进行扭曲
img=img.filter(ImageFilter.EDGE_ENHANCE_MORE)








img.show()
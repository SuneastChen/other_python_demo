import sys
import difflib

# first_path = sys.argv[1]  #a.txt
# next_path = sys.argv[2]  #b.txt
# #用来在命令行传参 python 文件对比.py a.txt b.txt

first_path='a.txt'
next_path='b.txt'




with open(first_path,'r') as f:
    first_list = f.readlines()
with open(next_path,'r') as f:
    next_list = f.readlines()

#创建Html对比的对象
diff = difflib.HtmlDiff()
html =diff.make_file(first_list,next_list)
# print(html)

with open('diff.html','w') as f:
    f.write(html)     



#创建内容对对对象
diff = difflib.Differ()
content = diff.compare(first_list,next_list)
for i in content:
    print(i)
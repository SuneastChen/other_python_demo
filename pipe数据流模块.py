from pipe import *

#求1到4求和
a1=range(5) | add
print(a1)


#求偶数和需要使用到where，作用类似于内建函数filter，过滤出符合条件的元素
a2=range(10) | where(lambda x:x%2==0) | add
print(a2)


#take_while函数用来指定范围
def one():
    i = 0
    while 1:
        i += 1
        if i % 13==0:
            yield i

#之前的写法如下:      
# for j in one():    
#     if i>100:
#         break
#     print(j)

a3=one() | where(lambda x : x%2==0) | take_while(lambda x : x<101) | as_list
print(a3)    #[26, 52, 78]


#需要对元素应用某个函数可以使用select，作用类似于内建函数map；需要得到一个列表，可以使用as_list：
a4=one() | where(lambda x : x%2==0) | take_while(lambda x : x<101) | select(lambda x:x*2) | as_list
print(a4)    #[52, 104, 156]


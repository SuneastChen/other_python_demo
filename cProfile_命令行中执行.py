


def test():
    totle=0
    for i in range(10**7):
        totle+=i
    print(totle)
test()


#shell中运行:
#python -m cProfile xxx\xxx.py     #直接把分析结果打印到控制台
#python -m cProfile -o result.prf xxx\xxx.py    #把分析结果保存到文件中
#python -m cProfile -s tottime xxx\xxx.py    #增加排序方式

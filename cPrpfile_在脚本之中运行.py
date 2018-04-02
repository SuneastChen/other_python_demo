
import cProfile

def test():
    totle=0
    for i in range(10**7):
        totle+=i
    print(totle)    

cProfile.run('test()')   #开始运行
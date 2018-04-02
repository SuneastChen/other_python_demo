
from memory_profiler import profile
@profile
def test():
    totle=0
    for i in range(1000):
        totle+=i
    print(totle)
    del totle
        
test()





@profile
def test():
    totle=0
    for i in range(10**5):
        totle+=i
        
test()

#cmd中切换到 kernprof.py 文件的路径下
#     cd C:\Python34\lib\site-packages
#python kernprof.py -l -v C:\Users\cxd\Desktop\line_profiler_test1.py
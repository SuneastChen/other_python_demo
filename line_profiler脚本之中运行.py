import line_profiler
import sys

def test():
    totle=0
    for i in range(10**5):
        totle+=i
        
prof=line_profiler.LineProfiler(test)  #创建 一个对象
prof.enable()   #开始性能分析
test()    #执行函数
prof.disable()   #停止性能分析
prof.print_stats(sys.stdout)   #打印

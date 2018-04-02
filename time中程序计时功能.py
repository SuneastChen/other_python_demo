
import time
def text():
    totle=0
    for i in range(10**7):
        totle+=i
    print('totle:',totle)  
    time.sleep(5)

print(time.clock()) 
text()
print(time.clock())

print(time.process_time())
print(time.perf_counter())
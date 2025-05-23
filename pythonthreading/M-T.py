from threading import *
import time
from time import sleep

def printeven():
    for i in range(0,11):
        if i % 2==0:
            print("even",i)
            sleep(1)
def printodd():
    for i in range(0,11):
        if i%2!=0:
            print("odd",i)
            sleep(1.1)


start_time= time.time()

t1=Thread(target=printeven)
t2=Thread(target=printodd)

t1.start()
t2.start()

t1.join()
t2.join()

end_time=time.time()

executed_time= end_time-start_time
print("Execution time is ", executed_time)
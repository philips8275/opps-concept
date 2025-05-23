from threading import *
from time import sleep


class Mythread(Thread):
    def run(self):
        for i in range(0,11):
            print(i)
            sleep(0.5)

class Mythread2(Thread):
    def run(self):
        for i in range(1,5):
            print(i)
            sleep(0.6)


t1= Mythread()

t2=Mythread2()

t1.start()
t1.join()

t2.start()
t2.join()

print("check ...!")
# Parametrized function as thread
# pass argument array to args attribute of thread constructor

import threading
from threading import *

def hello(name):
    for i in range(1,6):
        print("Hello..", name,1)

t1=threading.Thread(target=hello, args = ('Ram',))
t2=threading.Thread(target=hello, args= ('Shyam',))

t1.start()
t2.start()


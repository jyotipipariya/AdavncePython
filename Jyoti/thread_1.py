import threading
from threading import *

def hello():
    for i in range(1,5):
        print("Hello...", i)
def hi():
    for i in range(1,5):
        print("Hi..", i)

t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hi)

t1.start()
t2.start()

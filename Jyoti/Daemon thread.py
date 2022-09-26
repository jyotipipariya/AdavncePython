# Daemon Thread

import threading
from threading import *
import time
def first_thread():
    for i in range(1,7):
        time.sleep(4)
        print ("first_thread, deamon")

def second_thread():
    for i in range(1,4):
        time.sleep(2)
        print("second_thread, non-deamon")
t1=threading.Thread(target=first_thread)
t2=threading.Thread(target=second_thread)

t1.start()
time.sleep(4)
t2.start()
time.sleep(2)

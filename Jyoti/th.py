# Inherit Thread class
# Inherit Thread class and override run() method

import threading
from threading import *

class Hi(Thread):
    def run(self):
        for i in range(1,6):
            print("Hi..",i)

# create thread
t1=Hi()
# start thread
t1.start()

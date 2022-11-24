#Process : An instance of a program ex: Python interpreter
# * Takes advantages of multiple cpu and cores
# * Separate memory space ->memory is not shared between processes
# *great for cpu-bound processing
#     * New process is started independently  from other process
#     * One GIL for each process -> avoids GIL limitation
#
#     - Heavyweight
#     - Starting a process  is slower than starting threading
#     - MOre memory
#     IPC inter-process comunication is more complicated

#Threads : An entity within a process that can be scheduled false known as "Leightweight process"
# a process can spawn mutiple  threads
# - All threads within a process share the same memory
# - starting a thread is faster than starting a process
# - great for I/O - bound tasks
#
#     Threading is limited by GIL : only one thread at a time
#     - no effect for cpu-bound tasks
#         - not interruptable / Killable
#         - Careful with  race conditions
#
# GIL: Global interprter lock
# - A lock that allows only one thread at a time to exctute in python
#
# - Needed in CPython because memory management is not thread-safe
# Avoid:

# - uSE multiprocessing
# -use a different, free-threaded python implemention
# -use python as a wrapper for third-party libaries
#

from multiprocessing import Process
import os
import time

def squrae_number():
    for i in range(100):
        i*i
        time.sleep(0.1)
process =[]
numberofpr =os.cpu_count()

#create a process

for i in range(numberofpr):
    p= Process(target=squrae_number)
process.append(p)

#start
for p in process:
    p.start()

#join
for p in process:
    p.join()
    print("End main")

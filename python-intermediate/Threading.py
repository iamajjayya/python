from threading import Thread,Lock , current_thread
import  time

# database_value =0
#
# def increase(lock):
#     global  database_value
#     lock.acquire()
#     # processing
#     local_copy = database_value
#     local_copy += 1
#     time.sleep(0.01)
#     database_value = local_copy
#
#     lock.release()
#
#
# if __name__ == "__main__":
#     lock =Lock()
#     print("Start Value ", database_value)
#     thread1 = Thread(target=increase,args=(lock,))
#     thread2 = Thread(target=increase,args=(lock,))
#     thread3 = Thread(target=increase, args=(lock,))
#
#     thread1.start()
#     thread2.start()
#     thread3.start()
#
#     thread1.join()
#     thread2.join()
#     thread3.join()
#     print("End value",database_value)
#
#     print(" End Main")
from queue import  Queue

if __name__ == "__main__":
    q = Queue()
    # q.put("hello")
    # q.put(2)
    # q.put(3)
    #
    # first = q.get()
    # print(first)
    #
    # q.task_done()
    # q.join()
    def worker(q):
        while True:
            value= q.get()

            print(f" Threads couting in {current_thread().name} got {value} ")
            q.join()
            q.task_done()

    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker,args=(q,))
        thread.daemon=True
        thread.start()

    for i in range(1,21):
        q.put(i)
    q.join()
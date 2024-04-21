from threading import Thread, Lock
import time
from queue import Queue

database_value = 0

def increase(lock):
    global database_value
    
    with lock:
        local_copy = database_value
        # processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":
    
    lock = Lock()
    print('start value', database_value)
    thread1 = Thread(target=increase, args=(lock) )
    thread2 = Thread(target=increase, args=(lock) )
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print('end value', database_value)  
    print('end main')
    
def worker(q, lock):
    while True:
        value = q.get()
        # processing ...
        print(f'in {current_thread().name} got {value}')
        
    
    
q = Queue()
q.put(1)
q.put(2)
q.put(3)

# 3 2 1 ---> 
first = q.get()
print(first)
q.task_done()
q.join()

import threading
from queue import Queue


fibo_dict = {}
shared_queue = Queue()
input_list = [3, 10, 5, 7]

queue_condition = threading.Condition()

def fibonacci_task(condition):
    with condition:
        while shared_queue.empty():
            print(f"{threading.current_thread().name} - waiting for elements in queue...")
            condition.wait()
        else:
            value = shared_queue.get()
            a, b = 0, 1
            for _ in range(value):
                a, b = b, a + b
                fibo_dict[value] = a
        # shared_queue.task_done()
        print(f"{threading.current_thread().name}: fibo of key {value} with result {fibo_dict[value]}")

def queue_task(condition):
    print("Starting queue_task...")
    with condition:
        for i in input_list:
            shared_queue.put(i)
        condition.notifyAll()
        
threads = [threading.Thread(daemon=True, target=fibonacci_task, args=(queue_condition, )) for _ in range(4)]
for thread in threads:
    thread.start()

prod = threading.Thread(name='queue_task_thread', daemon=True, target=queue_task, args=(queue_condition,))
prod.start()

for thread in threads:
    thread.join()
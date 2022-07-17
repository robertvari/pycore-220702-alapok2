import random, time, threading


def worker1():
    print(f"Worker1 started on {threading.current_thread().name}")
    time.sleep(random.randint(4, 10))
    print("Worker1 finished!")


def worker2():
    print(f"Worker2 started on {threading.current_thread().name}")
    time.sleep(random.randint(4, 10))
    print("Worker2 finished!")


def worker3():
    print(f"Worker3 started on {threading.current_thread().name}")
    time.sleep(random.randint(4, 10))
    print("Worker3 finished!")


# pass as reference
t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)
t3 = threading.Thread(target=worker3)

t1.start()
t2.start()
t3.start()

# reference to the location in memory
# worker1

# call the function
# worker1()
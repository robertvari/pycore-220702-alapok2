import random, time
from my_python_library.decorators import timer


@timer
def worker1():
    print("Worker1 started...")
    time.sleep(random.randint(1, 6))
    print("Worker1 finished!")


@timer
def worker2():
    print("Worker2 started...")
    time.sleep(random.randint(1, 6))
    print("Worker2 finished!")


@timer
def worker3():
    print("Worker3 started...")
    time.sleep(random.randint(1, 6))
    print("Worker3 finished!")


worker1()
worker2()
worker3()
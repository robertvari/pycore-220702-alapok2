import random, time


def worker1():
    print("Worker1 started...")
    time.sleep(random.randint(1, 6))
    print("Worker1 finished!")


def worker2():
    print("Worker2 started...")
    time.sleep(random.randint(1, 6))
    print("Worker2 finished!")


def worker3():
    print("Worker3 started...")
    time.sleep(random.randint(1, 6))
    print("Worker3 finished!")


start = time.time()
worker1()
stop = time.time()

print(f"Worker1 processtime: {stop - start}")

start = time.time()
worker2()
stop = time.time()
print(f"Worker2 processtime: {stop - start}")


start = time.time()
worker3()
stop = time.time()
print(f"Worker3 processtime: {stop - start}")
import os, time, random, queue

# create a list of files
import threading

root_folder = r"C:\Work\_PythonSuli\pycore-220702\photos"
files = os.listdir(root_folder)

# create a job queue for threading
job_queue = queue.Queue()
for i in files:
    job_queue.put(i)


def worker():
    while not job_queue.empty():
        file = job_queue.get()
        print(f"Working on: {file}")
        time.sleep(random.randint(1, 10))
        print(f"---Worker finished: {file}")
        job_queue.task_done()


for _ in range(100):
    t = threading.Thread(target=worker)
    t.start()
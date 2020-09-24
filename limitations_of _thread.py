import threading
import time
import statistics
def read_data():
    with open("Emails.csv") as f:
        data = f.read()
        
times = []
for i in range(100):
    start = time.time()
    read_data()
    end = time.time()
    times.append(end - start)

threaded_times = []
for i in range(100):
    start = time.time()

    t1 = threading.Thread(target=read_data)
    t2 = threading.Thread(target=read_data)
    t1.start()
    t2.start()

    for thread in [t1, t2]:
        thread.join()

    end = time.time()
    
    
    
    

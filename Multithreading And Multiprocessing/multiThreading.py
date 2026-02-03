## Multithreading 
## when ton use this ?
# when we have task which spend more time waiting for I/O operations [eg : network request, file operation]
# concurrent execution: When you  
import threading
import time 

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"\n Numbers:{i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2) # isse hamra output 2 sec gap lekr chlega
        print(f"\n Letters:{letter}")
# create 2 threads
t1 = threading.Thread(target=print_numbers)
t2=  threading.Thread(target= print_letters)

# start the thread 
t1.start()
t2.start()

# wait for the threads to complete 

t1 = t1.join()
t2= t2.join()

t = time.time()
finished_time =time.time()-t
print(finished_time)
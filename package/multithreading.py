import threading
import time
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")

def print_letter():
    for i in "abcde":
        time.sleep(1)
        print(f"Letter: {i}")

# Creating new threads 
t1 = threading.Thread(target= print_numbers)
t2 = threading.Thread(target= print_letter)

t = time.time()
##print_numbers()
#print_letter()
t1.start()
t2.start()
## wait for the threads to complete
t1.join()
t2.join()
finished_time = time.time()-t
print("Time taken without threading:", finished_time)
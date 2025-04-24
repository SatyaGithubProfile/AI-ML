import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")


def print_let():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter : {letter}")

t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_let)

t = time.time()
# print_number()
# print_let()
t1.start()
t2.start()


#wait for threas to complete
t1.join()
t2.join()
finshTime = time.time()-t
print(finshTime)
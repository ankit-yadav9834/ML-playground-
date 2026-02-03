## Multiprocessing with "ProcessPoolExecutor"

from concurrent.futures import ProcessPoolExecutor
import time 

def square_numbers(number):
        time.sleep(1)
        return f"Square :{number*number}"
    
numbers = [1,2,3,4,5,6,7,8,9]


if __name__ == "__main__": # this is very important for handling error and this is entry point 
    with ProcessPoolExecutor(max_workers = 3) as executor:
        results = executor.map(square_numbers,numbers)

    for result in results:
        print(result)
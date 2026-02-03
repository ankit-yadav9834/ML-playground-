'''

Real- World Example: Multiprocessig for CPU- bound tasks 
Scenario: Factorial calculation 
Factorial calculation, escpecially for large numbers,
involve significant computation work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import time
import math
import sys

## Increasing the maximum number of digits for Integer conversion
sys.set_int_max_str_digits(100000)


# function to compute factorial of a given number 

def compute_factorial(number):
    print(f"Computing the factorail of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__== "__main__":
    numbers = [5000,6000,7000,8000]
    
    start_time = time.time()

    # create a pool of worker process 
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Results : {results}")
    print(f"Timr taken : {end_time- start_time} seconds")
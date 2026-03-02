'''Shows a certain number of the fibonacci sequence depending on how many digits the user asks'''

import sys
sys.set_int_max_str_digits(999999999)
fibonacci_list = [1, 1]
change = False
n = 0

while change == False:
    try:
        final_number = int(input("How many terms of the fibonacci sequence would you like to see? "))
        change = True
    except ValueError:
        print("That's not a number!")

# Fibonacci sequence

while n < final_number:
    sum_of_last_digits = fibonacci_list[-1] + fibonacci_list[-2]
    fibonacci_list[0] = fibonacci_list[1]
    fibonacci_list[1] = sum_of_last_digits
    n+= 1

print(fibonacci_list[-1])

import time
print(f"Took {time.process_time()} seconds to run.")
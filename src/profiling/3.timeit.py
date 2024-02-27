# pip3 install codetiming
import time
from timeit import timeit

def go_to_sleep():
    time.sleep(2)


def just_a_loop():
    for i in range(100_000_000):
        pass

iterations = 5
for function in go_to_sleep, just_a_loop:
    total_time = timeit("function()", number=iterations, globals=globals())
    avg = total_time / iterations
    print(f" Avg time: {avg:.2f} seconds")  # CPU time

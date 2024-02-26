import time

def go_to_sleep():
    time.sleep(2)


def just_a_loop():
    for i in range(100_000_000):
        pass


for function in go_to_sleep, just_a_loop:
    t1 = time.perf_counter(), time.process_time()
    function()
    t2 = time.perf_counter(), time.process_time()
    print(f"{function.__name__}()")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds") # Wall clock time
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")  # CPU time

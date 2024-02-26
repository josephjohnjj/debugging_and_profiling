# pip3 install codetiming
import time
from codetiming import Timer

def go_to_sleep():
    time.sleep(2)


def just_a_loop():
    for i in range(100_000_000):
        pass

@Timer(name="SleepCode", text="CPU time: {milliseconds:.0f} ms", initial_text="Time for {name} started")
def wrapper_go_to_sleep():
    go_to_sleep()

@Timer(name="LoopCode", text="CPU time: {milliseconds:.0f} ms", initial_text="Time for {name} started")
def wrapper_just_a_loop():
    just_a_loop()


for function in wrapper_go_to_sleep, wrapper_just_a_loop:
    function()

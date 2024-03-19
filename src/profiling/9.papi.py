from pypapi import papi_low as papi
from pypapi import events

import random

# Function to estimate the value of pi using Monte Carlo methods
def calculate_pi(tot_points):
    points_inside = 0
    for i in range(tot_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points_inside += 1
    pi_estimate = 4 * points_inside / tot_points
    return pi_estimate

papi.library_init()

evs = papi.create_eventset()
papi.add_event(evs, events.PAPI_DP_OPS)
papi.add_event(evs, events.PAPI_L1_DCM)

papi.start(evs)

pi = calculate_pi(100000)

result = papi.stop(evs)
print(pi)
print(result)

papi.cleanup_eventset(evs)
papi.destroy_eventset(evs)
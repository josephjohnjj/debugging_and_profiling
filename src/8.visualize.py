import cProfile
from cProfile import Profile
import numpy as np


N = 400000

def create_array(n):
    arr = np.arange(n)
    return arr

def numpy_multiple(arr1, arr2):
    result = np.multiply(arr1, arr2)

def slow_multiply(arr1, arr2):
    result = []

    for i in range (0, N):
        result.append(arr1[i] * arr2[i])


def main():
    arr1 = create_array(N)
    arr2 = create_array(N)

    profiler = Profile()
    profiler.enable()
    profiler.runctx('numpy_multiple(arr1, arr2)', globals(), locals())
    profiler.disable()
    profiler.dump_stats("numpy_multiple.prof")
    
if __name__ == '__main__':
    main()
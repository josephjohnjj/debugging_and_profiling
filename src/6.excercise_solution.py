import cProfile
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

    numpy_multiple(arr1, arr2)
    slow_multiply(arr1, arr2)


if __name__ == '__main__':
    print('Start profiling')
    cProfile.run('main()')
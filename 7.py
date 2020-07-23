from base import *
import numpy as np
from typing import List


def numpy_heavy_create_dot(number, base):
    start = time.time() - base
    DIMS = 3000
    a = np.random.rand(DIMS, DIMS)
    b = np.random.rand(DIMS, DIMS)
    np.dot(a, b)
    stop = time.time() - base
    return start, stop


nums = range(1, 8)

run_test(numpy_heavy_create_dot, nums)

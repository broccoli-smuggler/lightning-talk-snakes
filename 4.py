from base import *
import numpy as np
from typing import List


def numpy_heavy_dot(a_b: List[np.array], base):
    start = time.time() - base
    np.dot(*a_b)
    stop = time.time() - base
    return start, stop


DIMS = 3000
a = np.random.rand(DIMS, DIMS)
b = np.random.rand(DIMS, DIMS)

a_b_arr = [(a, b)] * 8

run_test(numpy_heavy_dot, a_b_arr)

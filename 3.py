from base import *


def cpu_heavy(n, base):
    start = time.time() - base
    count = 0
    for i in range(n):
        count += i
    stop = time.time() - base
    return start, stop


nums = [5**9] * 8

run_test(cpu_heavy, nums)


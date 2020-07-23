from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import numpy as np
import time
import matplotlib.pyplot as plt
from functools import partial


def visualize_runtimes(results, title):
    start, stop = np.array(results).T
    plt.barh(range(len(start)), stop-start, left=start)
    plt.grid(axis='x')
    plt.ylabel("Tasks")
    plt.xlabel("Seconds")
    plt.title(title)
    plt.show()
    print(title)
    return stop[-1]-start[0]


def multi(func, args, executor):
    res = (None, None)
    try:
        begin_time = time.time()
        res = executor.map(func, args, [begin_time] * len(args))
    except Exception as e:
        print('ERROR: %s' % e)
    return list(res)


def multiprocessing(func, args, workers=None):
    with ProcessPoolExecutor(max_workers=workers) as executor:
        res = multi(func, args, executor)
    return list(res)


def multithreading(func, args, workers=None):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        res = multi(func, args, executor)
    return list(res)


singlethreading = partial(multithreading, workers=1)


def run_test(func, input):
    visualize_runtimes(singlethreading(func, input), singlethreading.func.__name__ + ":1 " + func.__name__)
    visualize_runtimes(multithreading(func, input, 4), multithreading.__name__ + ":4 " + func.__name__)
    visualize_runtimes(multiprocessing(func, input, 4), multiprocessing.__name__ + ":4 " + func.__name__)
    print("done")

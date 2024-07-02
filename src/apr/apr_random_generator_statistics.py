import random as rand
from timeit import timeit
import sys


def rand_analysis_a(value_span, num_of_rands):
    collection = []
    for _ in range(num_of_rands):
        r = rand.randint(1, value_span)
        i = 0
        while i < len(collection) and collection[i][0] != r:
            i += 1
        if i < len(collection):
            collection[i] = (r, collection[i][1] + 1)
        else:
            collection.append((r, 1))
    return collection


def rand_analysis_b(value_span, num_of_rands):
    def bin_search(c, x):
        low, high = -1, len(c)
        while low + 1 != high:
            m = (low + high) // 2
            if c[m][0] < x:
                low = m
            elif c[m][0] > x:
                high = m
            else:
                return m
        return high

    collection = []
    for _ in range(num_of_rands):
        r = rand.randint(1, value_span)
        i = bin_search(collection, r)
        if i < len(collection) and collection[i][0] == r:
            collection[i] = (r, collection[i][1] + 1)
        else:
            collection.insert(i, (r, 1))
    return collection


def rand_analysis_c(value_span, num_of_rands):
    collection = [0] * value_span
    for _ in range(num_of_rands):
        r = rand.randint(1, value_span)
        collection[r - 1] += 1
    return collection


def rand_analysis_d(value_span, num_of_rands):
    collection = dict()
    for _ in range(num_of_rands):
        r = rand.randint(1, value_span)
        collection[r] = collection.get(r, 0) + 1
    return collection


def measure_time(func):
    n = 1000
    rand.seed(42)
    t1 = timeit(lambda: func(n, 10 * n), number=10)
    print(func.__name__, t1, end=' ')
    n *= 2
    rand.seed(42)
    t2 = timeit(lambda: func(n, 10 * n), number=10)
    print(t2, t2 / t1)


def run_func(func):
    rand.seed(42)
    res = func(10, 100)
    print(func.__name__, res, sys.getsizeof(res))


def run_for_all(func, func_list):
    for f in func_list:
        func(f)


def main():
    func_list = [rand_analysis_a, rand_analysis_b, rand_analysis_c, rand_analysis_d]
    run_for_all(run_func, func_list)
    run_for_all(measure_time, func_list)


if __name__ == '__main__':
    main()

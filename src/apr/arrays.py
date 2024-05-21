import random
import sys
from timeit import timeit


def a1(n):
    x = dict()
    for i in range(n * 10):
        y = random.randint(0, n)
        x[y] = x.get(y, 0) + 1
    return x


def a2(n):
    x = [0] * (n + 1)
    for _ in range(n * 10):
        y = random.randint(0, n)
        x[y] += 1
    return x


def measure_time(func):
    n = 1000
    random.seed(42)
    t1 = timeit(lambda: func(n), number=10)
    print(func.__name__, t1, end=' ')
    n *= 2
    random.seed(42)
    t2 = timeit(lambda: func(n), number=10)
    print(t2, t2 / t1)


def run_func(func):
    random.seed(42)
    res = func(10)
    print(func.__name__, res, sys.getsizeof(res))


def run_for_all(func, func_list):
    for f in func_list:
        func(f)


def main():
    func_list = [a1, a2]
    run_for_all(run_func, func_list)
    run_for_all(measure_time, func_list)


if __name__ == '__main__':
    main()

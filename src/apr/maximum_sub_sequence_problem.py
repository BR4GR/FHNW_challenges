import random
import time as t
import math

input = [31, -41, 59, 26, -53, 58, 97, -93, -23]

def alg1(list):
    ll =len(list)
    max_win = 0
    for i in range(ll):
        for j in range(i, ll):
            if sum(list[i:j+1]) > max_win:
                max_win = sum(list[i:j+1])
    print(max_win)


def list_comprehention(list):
    print(max([0] + [sum(list[s:e + 1]) for s in range(len(list)) for e in range(s, len(list))]))

def kadanes_algorithm(list):
    max = 0
    max_so_far = 0
    for i in range(len(list)):
        max_so_far = max_so_far + list[i]
        if max_so_far < 0:
            max_so_far = 0
        if max_so_far > max:
            max = max_so_far


if __name__ == '__main__':
    for i in range(20):
        sample = [random.randint(-100, 100) for _ in range(9*2**i)]
        print (9*2**i)
        start = t.time()
        kadanes_algorithm(sample)
        end = t.time()
        print(end-start)
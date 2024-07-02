from time import time_ns

import numpy as np

input = [4, 9, 6, 1, 3, 8, 5, 2, 7]
test_input = [3, 8, 9, 1, 2, 5, 4, 6, 7]  # test input
test_answer = 149245887792
answer = 218882971435

st = time_ns()

MAX = 1_000_000
input = list(range(MAX + 2))
input.pop(0)
input[3] = 8
input[8] = 9
input[9] = 1
input[1] = 2
input[2] = 5
input[5] = 4
input[4] = 6
input[6] = 7
input[7] = 10
input[MAX] = 3
current = 3
print(input[:20])

for i in range(10_000_000):
    a = input[current]
    b = input[a]
    c = input[b]

    destination = current - 1
    while destination == a or destination == b or destination == c or destination == 0:
        destination = destination - 1
        if destination <= 0:
            destination = MAX
    input[current] = input[c]
    destination_points_to = input[destination]
    input[c] = input[destination]
    input[destination] = a
    current = input[current]


a = input[1]
b = input[a]
res = a * b
print(f"-- final --")
print(f"{a} * {b} = {res}")

et = time_ns()
elapsed = et - st

print(f"took {elapsed} nanoseconds")
print(f"which is {elapsed/ 1000_000_000} seconds")

# 934001 * 159792 = 149245887792
# took 6675766274 nanoseconds
# which is 6.675766274 seconds

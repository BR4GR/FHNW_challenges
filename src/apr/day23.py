import timeit
import numpy as np

input = [4, 9, 6, 1, 3, 8, 5, 2, 7]
test_result = 67384529


def solve():
    input = [3, 8, 9, 1, 2, 5, 4, 6, 7]  # test input
    mod = len(input) + 1
    i = 0
    current_index = i
    mod = len(input) + 1

    for _ in range(100):
        current_value = input[(current_index)]
        a = input.pop(current_index + 1 if current_index + 1 < len(input) else 0)
        b = input.pop(((current_index + 1) if current_index + 1 < len(input) else 0))
        c = input.pop(((current_index + 1) if current_index + 1 < len(input) else 0))
        destination_value = (current_value - 1) % mod

        while destination_value not in input:
            destination_value = (destination_value - 1) % mod
        destination_index = input.index(destination_value)

        input.insert((destination_index + 1), c)
        input.insert((destination_index + 1), b)
        input.insert((destination_index + 1), a)
        current_index = input.index(current_value) + 1
        if current_index == mod - 1:
            current_index = 0
        i = i + 1

    while input[0] != 1:
        input.append(input.pop(0))

    res = "".join(str(s) for s in input[1:])
    return res


def solve2():
    input = {
        3: 8,
        8: 9,
        9: 1,
        1: 2,
        2: 5,
        5: 4,
        4: 6,
        6: 7,
        7: 3,
    }
    MAX = 9
    current = 3
    for i in range(100):
        a = input[current]
        b = input[a]
        c = input[b]

        destination = current - 1
        while (
            destination == a or destination == b or destination == c or destination == 0
        ):
            destination = destination - 1 
            if destination < 1:
                destination = MAX
        input[current] = input[c]
        input[c] = input[destination]
        input[destination] = a
        current = input[current]
    res = ""
    step = 1
    while input[step] != 1:
        res += str(input[step])
        step = input[step]
    return res

def solve3():
    input = list(range(10))
    input[3] = 8
    input[8] = 9
    input[9] = 1
    input[1] = 2
    input[2] = 5
    input[5] = 4
    input[4] = 6
    input[6] = 7
    input[7] = 3
    MAX = 9
    current = 3

    for _ in range(100):
        a = input[current]
        b = input[a]
        c = input[b]

        destination = current - 1
        while (
            destination == a or destination == b or destination == c or destination == 0
        ):
            destination = destination - 1 
            if destination < 1:
                destination = MAX
        input[current] = input[c]
        input[c] = input[destination]
        input[destination] = a
        current = input[current]

    res = ""
    step = 1
    while input[step] != 1:
        res += str(input[step])
        step = input[step]
    return res

def solve4():
    input = np.arange(10)
    input[3] = 8
    input[8] = 9
    input[9] = 1
    input[1] = 2
    input[2] = 5
    input[5] = 4
    input[4] = 6
    input[6] = 7
    input[7] = 3
    MAX = 9
    current = 3

    for _ in range(100):
        a = input[current]
        b = input[a]
        c = input[b]

        destination = current - 1
        while (
            destination == a or destination == b or destination == c or destination == 0
        ):
            destination = destination - 1 
            if destination < 1:
                destination = MAX
        input[current] = input[c]
        input[c] = input[destination]
        input[destination] = a
        current = input[current]

    res = ""
    step = 1
    while input[step] != 1:
        res += str(input[step])
        step = input[step]
    return res

N_ITTERATIONS = 10_000
print(solve())
f1 = timeit.timeit(solve, number=N_ITTERATIONS)
print(f"solve primitive: {f1}")
print('this will not solve part 2\n')

print(solve2())
f2 = timeit.timeit(solve2, number=N_ITTERATIONS)
print(f"solve with dict as nodes: {f2}")
print(f"that's {f1/f2} times faster than primitive")
print('this solved part two in 9.784249715 seconds\n')

print(solve3())
f3 = timeit.timeit(solve3, number=N_ITTERATIONS)
print(f"solve using list indexes as nodes: {f3}")
print(f"that's {f1/f3} times faster than primitive")
print(f"and {f2/f3} times faster than the dict solution")
print('this solved part two in 6.675766274 seconds\n')

print(solve4())
f4 = timeit.timeit(solve4, number=N_ITTERATIONS)
print(f"solve using numpy indexes as nodes: {f4}")
print(f"that's {f1/f4} times faster than primitive")
print(f"and {f3/f4} times faster than the list index solution\n")
print('this solved part two in 12.487709971 seconds\n')

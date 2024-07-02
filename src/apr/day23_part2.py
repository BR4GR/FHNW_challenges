def solve_dict():
    from time import time_ns

    st = time_ns()
    MAX = 1_000_000
    input = {
        4: 9,
        9: 6,
        6: 1,
        1: 3,
        3: 8,
        8: 5,
        5: 2,
        2: 7,
        7: 10,
        1_000_000: 4,
    }
    current = 4

    for i in range(10, 1_000_000):
        input[i] = i + 1

    for i in range(10_000_000):
        a = input[current]
        b = input[a]
        c = input[b]

        destination = current - 1
        while (
            destination == a or destination == b or destination == c or destination == 0
        ):
            destination = destination - 1
            if destination <= 0:
                destination = MAX
        input[current] = input[c]
        input[c] = input[destination]
        input[destination] = a
        current = input[current]

    a = input[1]
    b = input[a]
    res = a * b

    et = time_ns()
    elapsed = et - st

    print("solving using a dict.")
    print(f"{a} * {b} = {res}")
    print(f"took {elapsed} nanoseconds")
    print(f"which is {elapsed/ 1_000_000_000} seconds\n")


solve_dict()


def solve_np():
    from time import time_ns

    import numpy as np

    input = [4, 9, 6, 1, 3, 8, 5, 2, 7]

    st = time_ns()
    MAX = 1_000_000
    input = np.arange(MAX + 2)
    input = input + 1
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

    for i in range(10_000_000):
        a = input[current]
        b = input[a]
        c = input[b]

        destination = current - 1
        while (
            destination == a or destination == b or destination == c or destination == 0
        ):
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

    et = time_ns()
    elapsed = et - st

    print("\nsolving using a numpy.")
    print(f"{a} * {b} = {res}")
    print(f"took {elapsed} nanoseconds")
    print(f"which is {elapsed/ 1_000_000_000} seconds")


solve_np()


def solve_list():
    from time import time_ns

    import numpy as np

    st = time_ns()

    input = [4, 9, 6, 1, 3, 8, 5, 2, 7]
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

    for i in range(10_000_000):
        a = input[current]
        b = input[a]
        c = input[b]

        destination = current - 1
        while (
            destination == a or destination == b or destination == c or destination == 0
        ):
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

    et = time_ns()
    elapsed = et - st

    print("\nsolving using a list.")
    print(f"{a} * {b} = {res}")
    print(f"took {elapsed} nanoseconds")
    print(f"which is {elapsed/ 1_000_000_000} seconds")


solve_list()


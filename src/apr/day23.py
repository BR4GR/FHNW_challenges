input = [3, 8, 9, 1, 2, 5, 4, 6, 7]  # test input
input = [4, 9, 6, 1, 3, 8, 5, 2, 7]
test_result = 67384529

i = 0
current_index = i
mod = len(input) - 1

for _ in range(100):
    print(f"-- move {i + 1} --")
    print(f"cups: {input}")
    print(current_index % mod)
    current_value = input[(current_index)]
    a = input.pop(((current_index + 1) if current_index + 1 < len(input) else 0))
    b = input.pop(((current_index + 1) if current_index + 1 < len(input) else 0))
    c = input.pop(((current_index + 1) if current_index + 1 < len(input) else 0))
    destination_value = (current_value - 1) % 10
    print(f"current value: { current_value }")
    print(f"pick up: {a}, {b}, {c}")
    print(f"initial d: { destination_value }")
    print(f"cups: {input}")

    while destination_value not in input:
        destination_value = (destination_value - 1) % 10
    destination_index = input.index(destination_value)

    print(f"destination: { destination_value }")
    print(f"destination index: {destination_index}")
    print(f"                ")
    input.insert((destination_index + 1), c)
    input.insert((destination_index + 1), b)
    input.insert((destination_index + 1), a)
    current_index = input.index(current_value) + 1
    if current_index == 9:
        current_index = 0
    print(current_index)
    i = i + 1

print(f"-- final --")
print(f"cups: {input}")

while input[0] != 1:
    x = input.pop(0)
    input.append(x)

res = "".join(str(s) for s in input[1:])

print(res)

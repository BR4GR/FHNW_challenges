import random


def new_hash_set(table_size):
    return tuple([] for _ in range(table_size))


def add_to_hash_set(table, elem):
    index = hash(elem) % len(table)
    if elem not in table[index]:
        table[index].append(elem)


tab = new_hash_set(5)
print(tab)
add_to_hash_set(tab, 55)
add_to_hash_set(tab, '55')
add_to_hash_set(tab, 5)
add_to_hash_set(tab, 55)
add_to_hash_set(tab, 54)
add_to_hash_set(tab, '54')
print(tab)


def remove_from_hash_set(table, elem):
    index = hash(elem) % len(table)
    if elem in table[index]:
        table[index].remove(elem)


remove_from_hash_set(tab, 55)
print(tab)


def is_in_hash_set(t, e):
    i = hash(e) % len(t)
    return e in t[i]


print(is_in_hash_set(tab, 5))


def num_elems(t):
    return sum(len(x) for x in t)


print(num_elems(tab))


def get_statistics(table):
    looks = sum((len(n) * (len(n) + 1)) // 2 for n in table)
    max_len = max(len(x) for x in table)
    return looks, max_len


print(get_statistics(tab))
print('---------------------')

li = new_hash_set(400_000)
for _ in range(300_000):
    add_to_hash_set(li, random.random())
print(get_statistics(li))
li2 = new_hash_set(400_009)
for _ in range(300_000):
    add_to_hash_set(li2, random.random())
print(get_statistics(li2))
li3 = new_hash_set(3121)
for _ in range(300_000):
    add_to_hash_set(li3, random.random())
print(get_statistics(li3))


def add_to_hash_set_linear_probing(table, elem):
    h = hash(elem) % len(table)
    while table[h] is not None and table[h] != elem:
        h = (h + 1) % len(table)
        if table[h] is None:
            table[h] = elem


def add_to_hash_set_double_hashing(table, elem):
    h = hash(elem) % len(table)
    step = 1 + hash(elem) % (len(table) - 2)
    while table[h] is not None and table[h] != elem:
        h = (h + step) % len(table)
        if table[h] is None:
            table[h] = elem

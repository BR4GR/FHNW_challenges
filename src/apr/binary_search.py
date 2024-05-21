l1 = [1, 1, 2, 3, 5, 7, 8, 9, 9, 9, 12, 13, 14, 15, 17, 18, 21, 22, 24, 26, 27]
l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def bin_search(lst, value):
    low = -1
    high = len(lst)
    while high - low > 1 :
        x = (high + low) // 2
        if lst[x] == value:
            return x
        if lst[x] > value:
            high = x
        else:
            low = x
    return high


print(bin_search(l1, 30))

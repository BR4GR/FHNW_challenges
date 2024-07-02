a = ['blue', 'blue', 'red', 'red', 'red']

r, w, b = 0 , 0, len(a)

# Hier gilt die Invariante
while w != b:
    # Verschiebe schrittweise r, w, b unter Aufrechterhaltung der Invarianten,
    # so dass der Abstand zwischen b und w immer kleiner wird.
    cur = a[w]
    if cur == 'red':
        a[w] = 'white'
        w += 1
        a[r] = 'red'
        r += 1

    elif cur == 'white':
        w += 1
    else: # cur == 'blue' gilt
        b -= 1
        if b != w:
            a[w] = a[b]
            a[b] = 'blue'
    # Hier gilt die Invariante immer noch
    # Auch hier gilt die Invariante noch

    print(a)


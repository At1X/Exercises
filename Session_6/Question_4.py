def h(x):
    if x == 0:
        return 6
    elif x == 1:
        return -4
    elif x == 2:
        return 1
    return 4 * h(x - 1) - 2 * h(x - 2) + h(x - 3)


n = int(input())
print(h(n))

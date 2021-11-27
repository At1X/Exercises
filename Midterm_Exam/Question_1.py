def func(arr):
    lens = [0, 0, 0, 0, 0, 0]
    for elm in arr:
        lens[len(elm)] += 1
    return lens.index(max(lens))


arr = input().split()
print(func(arr))

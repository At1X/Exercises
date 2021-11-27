def func(x):
    y = int(str(x)[::-1])
    return abs(x - y)


x = int(input())
print(func(x))

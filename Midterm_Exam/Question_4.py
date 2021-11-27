def func(x, y):
    x += 4 if x % 4 == 3 else 3 - (x % 4)
    y -= 4 if y % 4 == 3 else 1 + (y % 4)
    return 0 if x > y else ((y - x) // 4) + 1


x, y = input().split()
print(func(int(x), int(y)))

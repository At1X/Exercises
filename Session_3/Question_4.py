x = int(input())

if x % 2 == 0:
    print(x // 2)
    print((x // 2) * "2 ")
else:
    print((x - 3) // 2 + 1)
    print("3 " + ((x - 3) // 2) * "2 ")

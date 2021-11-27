def func(arr):
    flag = True
    if len(arr) > 2:
        d = int(arr[1]) - int(arr[0])
        for i in range(2, len(arr)):
            if int(arr[i]) - int(arr[i - 1]) != d:
                flag = False
                break
    return flag


arr = input().split()
print(func(arr))

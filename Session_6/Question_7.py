def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)


a = int(input())
b = int(input())
print(GCD(a, b))

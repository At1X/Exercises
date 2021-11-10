n = int(input())

pow2 = 2
while n > pow2:
    pow2 *= 2

x = n - (pow2 // 2)
print(1 if n == pow2 else 2 * x + 1)

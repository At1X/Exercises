n = int(input())

num = ''
for i in range(1, n + 1):
    num += str(i)
digits = len(str(num))

print(int(num) // (10 ** (digits - n)) % 10)

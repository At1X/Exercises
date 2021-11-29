n = int(input())
num = ''

for base in range(1, n + 1):
    num += str(base)

temp_num = int(num)
digits = 0
while temp_num >= 1:
    temp_num //= 10
    digits += 1

print(int(num) // (10 ** (digits - n)) % 10)

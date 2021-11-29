def IUT_operator(num1, num2):
    res = ''
    for i, j in zip(str(num1), str(num2)):
        res += i + j
    return int(res)


def IUT_base_operator(num, base):
    if num == 0:
        return '0'
    digits = ''
    while num:
        digits += str(int(num % base))
        num //= base
    return digits[::-1]


def IUT_number(num):
    return num == int(str(num)[::-1])


a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = int(IUT_base_operator(IUT_operator(a, b), c), d)
print(x)
print(IUT_number(x))

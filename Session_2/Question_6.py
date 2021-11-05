def numberToBase(n, b):
    if n == 0:
        return "0"
    digits = ""
    while n:
        digits += str(int(n % b))
        n //= b
    return digits[::-1]


num_dices = int(input())
permutation = int(input())

permutation_base_6 = int(numberToBase(permutation - 1, 6))
ans = int(num_dices * '1') + permutation_base_6
print(ans)

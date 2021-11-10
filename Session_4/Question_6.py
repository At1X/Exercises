n = int(input())
prime = 2
ans = ''

while n >= prime:
    power = 0
    while n % prime == 0:
        power += 1
        n /= prime

    if power > 0:
        if ans != '':
            ans += '*'

        if power != 1:
            ans += str(prime) + '^' + str(power)
        else:
            ans += str(prime)

    prime += 1

print(ans)

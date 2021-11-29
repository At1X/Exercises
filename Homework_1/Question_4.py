def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


m = int(input())
n = int(input())

if (m + n) % 2 == 0:
    for i in range(m + 1, n):
        if (i == 5) or (i == 6) or (i % 100 == 25) or (i % 100 == 76):
            if (i ** 2 - i) % (10 ** len(str(i))) == 0:
                print(i, end=' ')
else:
    sum_primes = 0
    for i in range(m + 1, n):
        if is_prime(i):
            for j in str(i):
                sum_primes += int(j)
    print(sum_primes)

n = int(input())
cnt = 1
factoriel = 1

while n >= cnt:
    factoriel *= cnt
    cnt += 1

print(factoriel)

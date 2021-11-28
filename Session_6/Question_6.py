nab = list(map(int, input(). split()))
goals = list(map(int, input(). split()))

for i in range(nab[0] - 1):
    if goals[i] < goals[i + 1]:
        continue
    if goals[nab[0] - 1] <= (90 + nab[2]) and goals[i] <= 45 + nab[1]:
        print('YES')
    else:
        print('NO')
    break
else:
    if goals[nab[0] - 1] <= 90 + nab[2]:
        print('YES')
    else:
        print('NO')

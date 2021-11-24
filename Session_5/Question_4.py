n = int(input())
arr = input().split()

up = False
down = False
change = False
situation = ''

for num in range(1, n):
    num1 = int(arr[num])
    num2 = int(arr[num - 1])
    if num1 > num2:
        if situation == 'down' and change:
            print('No')
            break
        if situation == 'down' and not change:
            change = True
        situation = 'up'
    if num1 < num2:
        if situation == 'up' and change:
            print('No')
            break
        if situation == 'up' and not change:
            change = True
        situation = 'down'
    if num1 == num2 and change:
        print('No')
        break
else:
    print('Yes')

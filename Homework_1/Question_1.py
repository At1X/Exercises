n = int(input())
x = input()
for i in range(n):
    x1 = input()
    x2 = input()
    if x1 == x:
        x = x2
    elif x2 == x:
        x = x1
print(x)

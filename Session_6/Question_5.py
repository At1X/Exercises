def checker(hashtag, number):
    if hashtag == '#':
        return True
    if len(hashtag) > len(number):
        return False
    parts = hashtag.split('#')
    if len(parts) == 1:
        return str(number).startswith(parts[0]) or str(number)[::-1].startswith(parts[0][::-1])
    return str(number).startswith(parts[0]) and str(number)[::-1].startswith(parts[1][::-1])


def print_equation(a, b, c):
    print(f'{a} + {b} = {c}')


equation = input().split()
a = equation[0]
b = equation[2]
c = equation[4]

if '#' in a:
    ans = int(c) - int(b)
    print_equation(ans, b, c) if checker(a, str(ans)) else print(-1)
elif '#' in b:
    ans = int(c) - int(a)
    print_equation(a, ans, c) if checker(b, str(ans)) else print(-1)
else:
    ans = int(a) + int(b)
    print_equation(a, b, ans) if checker(c, str(ans)) else print(-1)

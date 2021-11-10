a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        print('IMPOSSIBLE')
    else:
        if c == 0:
            print("{:.3f}".format(0))
        else:
            print("{:.3f}".format(-c / b))
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('IMPOSSIBLE')
    elif delta == 0:
        if c == 0:
            print("{:.3f}".format(0))
        else:
            print("{:.3f}".format(-b / (2 * a)))
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        if x1 > x2:
            print("{:.3f}".format(x2))
            print("{:.3f}".format(x1))
        else:
            print("{:.3f}".format(x1))
            print("{:.3f}".format(x2))

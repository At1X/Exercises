a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
c1 = int(input())
c2 = int(input())
d1 = int(input())
d2 = int(input())
e1 = int(input())
e2 = int(input())

if a1 == b1 or a1 == c1 or a1 == d1 or a1 == e1 or b1 == c1 or b1 == d1 or b1 == e1 or c1 == d1 or c1 == e1 or d1 == e1:
    print("Yes")

elif a2 == b2 or a2 == c2 or a2 == d2 or a2 == e2 or b2 == c2 or b2 == d2 or b2 == e2 or c2 == d2 or c2 == e2 or d2 == e2:
    print("Yes")

elif b2-a2 == b1-a1 or c2-a2 == c1-a1 or d2-a2 == d1-a1 or e2-a2 == e1-a1:
    print("Yes")

elif b2-a2 == a1-b1 or c2-a2 == a1-c1 or d2-a2 == a1-d1 or e2-a2 == a1-e1:
    print("Yes")

elif c2-b2 == c1-b1 or d2-b2 == d1-b1 or e2-b2 == e1-b1 or d2-c2 == d1-c1 or e2-c2 == e1-c1 or e2-d2 == e1-d1:
    print("Yes")

elif c2-b2 == b1-c1 or d2-b2 == b1-d1 or e2-b2 == b1-e1 or d2-c2 == c1-d1 or e2-c2 == c1-e1 or e2-d2 == d1-e1:
    print("Yes")

else:
    print("No")

b = int(input())
c = int(input())
x = int(input())
y = int(input())
p = (((b**2)*x + (c**2)*y)/(x+y) - x*y)**(1/2)
print("{:.2f}".format(p))
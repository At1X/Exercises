n = int(input())

a0 = 'Zero'
a1 = 'One'
a2 = 'Two'
a3 = 'Three'
a4 = 'Four'

print(a0 * bool(n % 5 == 0))
print(a1 * bool(n % 5 == 1))
print(a2 * bool(n % 5 == 2))
print(a3 * bool(n % 5 == 3))
print(a4 * bool(n % 5 == 4))

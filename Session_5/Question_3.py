n = input().split()
a = int(n[0])
b = int(n[2])

total_candies = (2 * min(a, b)) - (a < b)
for i in range(1, 5):
    print((total_candies // 4) + (total_candies % 4 >= i), end=' ')

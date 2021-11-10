n = int(input())
cnt = 1
sum = 0

while cnt < n:
    if n % cnt == 0:
        sum += cnt
    cnt += 1

print("YES" if sum == n else "NO")

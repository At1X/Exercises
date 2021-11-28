nxk = input().split()
n = int(nxk[0])
x = int(nxk[1])
k = int(nxk[2])

channels = []
for _ in range(n):
    channels.append(input())

print(channels[(x - 1 + k) % n])

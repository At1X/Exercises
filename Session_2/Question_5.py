rad = int(input())
room = int(input())

val = room // rad
num_val = rad - (room % rad)
num_val_plus = room % rad

ans = (num_val * (val ** 2)) + (num_val_plus * ((val + 1) ** 2))
print(ans)

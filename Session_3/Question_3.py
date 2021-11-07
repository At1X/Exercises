x = int(input())
y = int(input())

reverseX = f'{x % 10}{(x // 10) % 10}{x // 100}'
reverseY = f'{y % 10}{(y // 10) % 10}{y // 100}'

if int(reverseX) > int(reverseY):
    print(f"{y} < {x}")
elif int(reverseX) == int(reverseY):
    print(f"{x} = {y}")
else:
    print(f"{x} < {y}")

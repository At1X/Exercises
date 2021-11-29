n = int(input())
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(n * '#')
    elif i <= n // 2:
        print('#' + (i - 2) * ' ' + '#' + (n - 2 * i) * ' ' + i * '#')
    elif i == (n // 2) + 1 and n % 2 != 0:
        print('#' + (i - 2) * ' ' + '#' + (n - i) * '#')
    else:
        print('#' + (n - i - 1) * ' ' + '#' +
              (2 * (i - 1) - n) * ' ' + (n - i + 1) * '#')

n = int(input())
main_words = input()
wrong_words = input()

blindness = 0
for i in range(n):
    if main_words[i] != wrong_words[i]:
        blindness += 1

print(blindness)

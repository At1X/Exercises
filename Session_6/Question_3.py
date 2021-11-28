def func(textOne, textTwo):
    index = 0
    for char in textOne:
        if char == textTwo[index]:
            index += 1
            if index >= len(textTwo):
                return "YES"
    return "NO"


counter = int(input())
while counter > 0:
    textOne = input()
    textTwo = input()
    result = func(textOne, textTwo)
    if result == "NO":
        result = func(textOne[::-1], textTwo)
    print(result)
    counter -= 1

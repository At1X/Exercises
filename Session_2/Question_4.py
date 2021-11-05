header_footer = "((())) ()(()) ()()() (())() (()())"*4
print(header_footer)

sum = 1 + 1 + 2 + 5 + 14 + 42 + 132 + 429 + 1430 + 4862 + 16796
print("Sum:" + "{:.2f}".format(sum))

average = sum/11
print("Average:" + "{:.2f}".format(average))

variance = (
    (1 - average) ** 2
    + (1 - average) ** 2
    + (2 - average) ** 2
    + (5 - average) ** 2
    + (14 - average) ** 2
    + (42 - average) ** 2
    + (132 - average) ** 2
    + (429 - average) ** 2
    + (1430 - average) ** 2
    + (4862 - average) ** 2
    + (16796 - average) ** 2
)/10
print("Variance:" + "{:.2f}".format(variance))

print(header_footer)

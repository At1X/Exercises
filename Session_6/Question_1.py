def swap_function(a, b):
    print(f'Before swap in function: a is {a} & b is {b}')
    a, b = b, a
    print(f'After swap in function: a is {a} & b is {b}')


nums = input('Enter two integers as a & b: ').split()
a = int(nums[0])
b = int(nums[1])

print(f'Before calling swap function: a is {a} & b is {b}')
swap_function(a, b)
print(f'After calling swap function: a is {a} & b is {b}')

'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    a = a+1
    print(a)
inc(5)

# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    return a+1
print(inc_return(2))

# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    sum = a + b
    return sum
print(sum(7, 2))

# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    sum_inc = sum(a, b)
    return sum_inc

print(sum_inc(8, 4))


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    is_even = a % 2 == 0
    return print(is_even)

is_even(6)

# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
   num = int(repeat)
   for sentences in range(num)
    return

 # hint: you can add strings together 
    # in order to concatenate them
    
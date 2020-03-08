# A square of squares
# You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

# Task
# Given an integral number, determine if it's a square number:

import math     # importing math module

def is_square(n):
    if n > 0 and math.sqrt(n) % 1 == 0:     # checking if number is > 0 and if it's square
        return True   # its square number
    else:
        return False  # fix me


print ('Should be TRUE', is_square(25))
print ('Should be TRUE', is_square(4))
print ('Should be TRUE', is_square(144))
print ('Should be FALSE', is_square(-5))
print ('Should be FALSE', is_square(11))
print ('Should be FALSE', is_square(10))
This is test sadas

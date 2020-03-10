# write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
# the string should start with a 1.
# a string with size 6 should return :'101010'.
# with size 4 should return : '1010'.
# with size 12 should return : '101010101010'.
# The size will always be positive and will only use whole numbers.

def stringy(size):
    new_string = ""     # defining new string
    new_string += int(size / 2) * "10"  # divide size by 2 and adding that many '10's
    if size % 2 != 0:               # if size will be odd number we need to add 1 at the end of new_string
        new_string += "1"
    return new_string

def stringy_better(size):   # same solution but cleaner code
    return "10" * (int(size / 2)) + "1" * (size % 2)

print(stringy(5))   # tests
print(stringy_better(5))
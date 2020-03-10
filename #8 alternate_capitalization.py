# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
# The input will be a lowercase string with no spaces.
# Good luck!



def capitalize(s):
    outcome = ["",""]
    i = 0
    for char in s:
        if i % 2 == 0:
            outcome[0] += char.capitalize()
            outcome[1] += char
            i += 1
        else:
            outcome[0] += char
            outcome[1] += char.capitalize()
            i += 1
    return outcome

print(capitalize("abracadabra")) # test
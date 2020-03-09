# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    slowo = ""   # defining new empty string for doubled word
    for char in s:      # loop going by every char in word s
        char = 2 * char     # for every char doubling it
        slowo += char   # adding doubled char to new string
    return slowo    # returning new string


print(double_char("Hey Kappa Kappa Hey Kappa! Testing method"))   # test
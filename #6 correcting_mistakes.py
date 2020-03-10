# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

def correct(string):
    correct_string = ''     # define new empty string
    for char in string:     # loop going through every char and replacing numbers with chars if needed
        if char == '5':
            correct_string += char.replace('5', 'S')
        elif char == '0':
            correct_string += char.replace('0', 'O')
        elif char == '1':
            correct_string += char.replace('1', 'I')
        else:
            correct_string += char
    return correct_string   # returning new string

    pass


def correct_other(string):
    return string.replace('1','I').replace('0','O').replace('5','S')    # way easier way without using loop but using .replace method for strings

print(correct('c0rrect 5tr1ng'))        # tests
print(correct_other('c0rrect 5tr1ng'))
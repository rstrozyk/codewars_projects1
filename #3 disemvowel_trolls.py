# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def disemvowel(string):
    new_string = ''  # creating new empty string - new_string
    for char in string:  # iteration on every character
        if not char in 'aeiouAEIOU':  # if the character is not vowel adding it to new_string
            new_string += char
    string = new_string  # ascribing new_string to string
    return string


disemvowel("This website is for losers LOL!")

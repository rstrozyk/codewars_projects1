# Create a method that will return "Even" or "Odd" for given int

def even_or_odd(number):
    if number % 2 == 0: # every even number divided by 2 gives rest 0
        return "Even"
    else:
        return "Odd"
print(even_or_odd(6))   # test
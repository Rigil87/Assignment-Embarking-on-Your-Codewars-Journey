# Function for determining if a number is even or odd.
# Basically just using modulus to determin if there is a remained when divided by two,
# if no remainded must be even, otherwise it is odd

def even_or_odd(number):
    if (number % 2) == 0:
        return "Even"
    else:
        return "Odd"

# This function converts a number to a string. It occurs to me this could be accomplished with
# f formatting as well

def number_to_string(num):
    return str(num)

# I struggled with this one. The important thing to remember is to set a starting point for the 
# count_vowels variable. In this case starting at 0. After that its easy. Use a for loop to count
# all the items in the string using .count
def get_count(sentence):
    count_vowels = 0
    for vowels in ['a', 'e', 'i', 'o', 'u']:
        count_vowels += sentence.count(vowels)
    return count_vowels
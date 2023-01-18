# Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.


def print_three_characters(text):

    if not type(text) is str:
        raise TypeError("Only string are allowed")

    first_char = text[0]
    middle_char = text[int(round(len(text) / 2, 0)) - 1]
    last_char = text[-1]

    return first_char, middle_char, last_char


assert print_three_characters('Hello') == (
  'H', 'e', 'o'), "The result should be '('H', 'e', 'o')'"

# Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.


def new_string_creating(s1, s2):

    if not type(s1) is str:
        raise TypeError("Only string are allowed")

    if not type(s2) is str:
        raise TypeError("Only string are allowed")

    s1_middle_len = int(len(s1) / 2)

    new_string_creating = s1[0:s1_middle_len] + s2 + s1[s1_middle_len:]

    return new_string_creating


assert new_string_creating("Nastia",  "Norenko") == "NasNorenkotia", "The result should be 'NasNorenkotia'"

# new_string_creating()

#   Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Example:
# str1 = PyNaTive
# yaivePNT


def charachters_ordering(text):

    if not type(text) is str:
        raise TypeError("Only string are allowed")

    lower_case = ''
    upper_case = ''

    for i in text:
        if i.islower():
            lower_case += i
        else:
            upper_case += i

    return lower_case + upper_case

assert charachters_ordering('PyNaTive') == "yaivePNT", "The result should be 'yaivePNT'"

# Count all letters, digits, and special symbols from a given string
# Given: str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbolsgit commit -m "commit message"

# Chars = 8
# Digits = 3
# Symbol = 4


def symbols_groupping(text):

    if not type(text) is str:
        raise TypeError("Only string are allowed")

    chars = 0
    digits = 0
    symbol = 0

    for i in text:
        if i.isdigit():
            digits += 1
        elif i.isalpha():
            chars += 1
        else:
            symbol += 1

    return "Chars = " + str(chars), "Digits = " + str(digits), "Symbol = " + str(symbol)


assert symbols_groupping("P@#yn26at^&i5ve") == ('Chars = 8', 'Digits = 3', 'Symbol = 4'), "The result should be '('Chars = 8', 'Digits = 3', 'Symbol = 4')'"

# Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
# Given: str1 = "PYnative29@#8496"
# Expected Outcome: Sum is: 38 Average is  6.333333333333333


def sum_and_average_of_digits(text):

    if not type(text) is str:
        raise TypeError("Only string are allowed")

    sum_of_digits = 0
    avg_of_digits = 0

    for i in text:
        if i.isdigit():
            sum_of_digits += int(i)
            avg_of_digits += 1

    return "Sum is: " + str(sum_of_digits), "Average is " + str(avg_of_digits)


assert sum_and_average_of_digits("PYnative29@#8496") == ('Sum is: 38', 'Average is 6'), "The result should be '('Sum is: 38', 'Average is 6')'"

# Remove special symbols / punctuation from a string
# Given: str1 = "/*Jon is @developer & musician"
# Expected Output:
# "Jon is developer musician"


def special_symbols_removing(text):

    if not type(text) is str:
        raise TypeError("Only string are allowed")

    cleaned_text = ''

    for i in text:
        if i.isalpha() or i == " ":
            cleaned_text += i

    cleaned_text_wo_spaces = cleaned_text.replace("  ", " ")

    return cleaned_text_wo_spaces


assert special_symbols_removing(
  "/*Jon is @developer & musician"
) == "Jon is developer musician", "The result should be 'Jon is developer musician'"

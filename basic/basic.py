# 1) Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

text = input("text something: ")

if type(text)!='str':
    str(text)

new_text= ''

for n, i in enumerate(text):
    if n % 2 == 0 and n != len(text)-1:
        new_text += "'" + i + "'" + ", "
    elif n % 2 == 0:
        new_text += "'" + i + "'"

print(new_text)


# 2) Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.
# For example:
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
# Note: n must be less than the length of the string.

def remove_chars(text, n):
    if len(text) <= n:
        print("n must be less than the length of the string")
    else:
        new_text = text[n:]
        print(new_text)

remove_chars("pynative", 4)

# 3)  Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

def checkFirstAndLastNumberComparison(input_list):
    print(True if input_list[0] == input_list[-1] else False)

checkFirstAndLastNumberComparison([1, 2, 4])
checkFirstAndLastNumberComparison([1, 2, 1])

# 4) Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

number_list = [1, 2, 5, 10, 11]

for i in number_list:
    if i % 5 == 0:
        print(i)

# 5) Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.
text = "Emma is not Emma."
print(text.count('Emma'))


# Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

text = 7536
text_str = str(text)
text_str_reverse_order = text_str[::-1]
print(' '.join(text_str_reverse_order))

# Format variables using a string.format() method.
# Write a program that reads 3 parameters (totalMoney, quantity, price) from the console.
# Use string.format() method to format the following three variables as per the expected output
# Output example:
# I have 1000 dollars so I can buy 3 football for 450.00 dollars.

totalMoney = input("totalMoney: ")
quantity = input("quantity: ")
price = input("price: ")

print(f'I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars.')


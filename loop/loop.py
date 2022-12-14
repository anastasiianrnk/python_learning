# Print First 10 natural numbers using while loop
#
for num in range(10):
    print(num+1)

# Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

given_number = input('type number: ')

total_sum = 0
for i in range(int(given_number)+1):
    total_sum += i
print(total_sum)

# Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

current_list = [5, 16, 10, 55, 100, 150, 158, 175, 550, 63, 17, 50]
new_list = []
for i in current_list:
    if i > 150:
        continue
    elif i > 500:
        break
    elif i % 5 == 0:
        new_list.append(i)

print(new_list)

# Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.

given_number = 75869
given_number_str = str(given_number)

n = 0

while n < len(given_number_str):
    n+=1

print(n)

# # Print list in reverse order using a loop
given_list = [11, 22, 33]
new_list = []

for index in range(len(given_list)):
    print(given_list[len(given_list)-index-1])

# Use else block to display a message “Done” after successful execution of for loop
# For example, the following loop will execute without any error.
# for i in range(5):
#     print(i)
# 0
# 1
# 2
# 3
# 4
# Done!
# var1
for i in range(5):
    print(i)
print("Done!")
# var2
for i in range(5):
    if i == max(range(5)):
        print(i)
        print("Done!")
    else:
        print(i)
# Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it.
# The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

list = [0, 1]

for i in range(0, 8):
    list.append(list[-1]+list[-2])

print(list)

# Find the factorial of a given number
# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1

factorial_of = int(input("factorial of : !"))

result = 1

for i in range(1, factorial_of+1):
    result *= i

print(result)

# Use a loop to display elements from a given list present at odd index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Expected output: 20 40 60 80 100

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for index, value in enumerate(my_list):
    if index % 2 != 0:
        print(my_list[index])
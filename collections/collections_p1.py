# Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.


def united_list(l1, l2):

    united_list = []
    for n, value in enumerate(l1):
        if n % 2 != 0:
            united_list.append(value)

    for n, value in enumerate(l2):
        if n % 2 == 0:
            united_list.append(value)

    return united_list


assert united_list(
    [1, 2, 3, 4],
    [5, 6, 7, 8]) == [2, 4, 5, 7], "Expected Outcome should be: [2, 4, 5, 7]"


# Slice list into 3 equal chunks and reverse each chunk
# Given: sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Expected Outcome:

# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]

# def slice_reverse_list(list):


def split_and_reverse_list(sample_list):
    count_of_parts = int(len(sample_list) / 3)

    if len(sample_list) % 3 != 0:
        raise Exception(
            "The number of list's elements can't be divided equally by 3!")

    start_of_list = 0
    end_of_list = count_of_parts
    name_num = []

    while end_of_list <= len(sample_list):
        name_num.append(start_of_list)
        globals()[f"list{start_of_list}"] = sample_list[start_of_list:end_of_list]
        start_of_list += count_of_parts
        end_of_list += count_of_parts

    result_list = []
    for i in name_num:
        # print(globals()[f"list{i}"][::-1])
        result_list.append(globals()[f"list{i}"][::-1])

    return result_list


assert split_and_reverse_list([11, 45, 8, 23, 14, 12, 78, 45, 89]) == [
    [8, 45, 11], [12, 14, 23], [89, 45, 78]
], "Expected Outcome should be: [[8, 45, 11], [12, 14, 23], [89, 45, 78]]"


# Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# Given:
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# Expected Outcome:
# After removing unwanted elements from list [47, 69, 76, 97]


def remove_spare_elements_from_list(sample_list, sample_dictionary):
    for i in sample_list.copy():
        if i not in sample_dictionary.values():
            sample_list.remove(i)
        else:
            continue

    return sample_list


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

assert remove_spare_elements_from_list([47, 64, 69, 37, 76, 83, 95, 97], {
    'Jhon': 47,
    'Emma': 69,
    'Kelly': 76,
    'Jason': 97
}) == [47, 69, 76, 97], "Expected Outcome should be: [47, 69, 76, 97]"


# Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# Expected Outcome:
# [47, 52, 44, 53, 54]


def list_from_dict_value(sample_dictionary):
    new_list = []

    for i in sample_dictionary.values():
        if i not in new_list:
            new_list.append(i)

    return new_list


speed = {
    'jan': 47,
    'feb': 52,
    'march': 47,
    'April': 44,
    'May': 52,
    'June': 53,
    'july': 54,
    'Aug': 44,
    'Sept': 54
}

assert list_from_dict_value(speed) == [
    47, 52, 44, 53, 54
], "Expected Outcome should be: [47, 52, 44, 53, 54]"


# Remove duplicates from a list and create a tuple and find the minimum and maximum number
# Given:
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# Expected Outcome:
# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99

def remove_duplicate(sample_list):
    count = 0

    for n, val in enumerate(sample_list.copy()):
        if val in sample_list.copy()[n + 1:]:
            sample_list.pop(n - count)
            count += 1

    unique_elements_tuple = tuple(sample_list)
    min_element = min(unique_elements_tuple)
    max_element = max(unique_elements_tuple)

    return sample_list, unique_elements_tuple, min_element, max_element


sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

assert remove_duplicate(sample_list) == ([87, 45, 65, 41, 99, 94], (87, 45, 65, 41, 99, 94), 41,
                                         99), "Expected Outcome should be: ([87, 45, 65, 41, 99, 94], (87, 45, 65, 41, 99, 94), 41, 99)"


# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output:
# [1, 4, 9, 16, 25, 36, 49]

def square_of_number(list_of_numbers):
    for i, val in enumerate(list_of_numbers):
        list_of_numbers[i] = val ** 2

    return list_of_numbers


numbers = [1, 2, 3, 4, 5, 6, 7]

assert square_of_number(numbers) == [1, 4, 9, 16, 25, 36, 49], "Expected Outcome should be: [1, 4, 9, 16, 25, 36, 49]"


#  Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def concatenate_two_lists(list1, list2):
    list3 = []
    cnt = 0

    for i in list1:
        for n in list2:
            list3.append(i + n)
            cnt += 1

    return list3


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

assert concatenate_two_lists(list1, list2) == ['Hello Dear', 'Hello Sir', 'take Dear',
                                               'take Sir'], "Expected Outcome should be: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']"


# Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]

def remove_empty_strings(sample_list):
    for i in range(len(sample_list) - 1, -1, -1):
        if sample_list[i] == "":
            sample_list.pop(i)
    return sample_list


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

assert remove_empty_strings(list1) == ["Mike", "Emma", "Kelly",
                                       "Brad"], "Expected Outcome should be: ['Mike', 'Emma', 'Kelly', 'Brad']"


# Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
# Given:
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:
# [5, 15, 25, 50]

def remove_all_twenty(sample_list):
    for i in sample_list:
        if i == 20:
            sample_list.remove(20)

    return sample_list


list1 = [5, 20, 15, 20, 25, 50, 20]

assert remove_all_twenty(list1) == [5, 15, 25, 50], "Expected Outcome should be: [5, 15, 25, 50]"


# Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

def create_dict_from_two_lists(keys_list, values_list):
    if len(keys_list) != len(values_list):
        raise Exception("The number of elements in the lists should be equal")

    sample_dict = {}

    for i in range(len(keys_list)):
        sample_dict[keys_list[i]] = values_list[i]

    return sample_dict


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

assert create_dict_from_two_lists(keys, values) == {'Ten': 10, 'Twenty': 20,
                                                    'Thirty': 30}, "Expected Outcome should be: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}"

# res = dict(zip(keys, values))

# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


def merge_two_dictionaries(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3


assert merge_two_dictionaries(dict1, dict2) == {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40,
                                                'Fifty': 50}, "Expected Outcome should be: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}"

#   Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# Expected output:
# 80

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


# print(sampleDict['class']['student']['marks']['history'])

# Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.
# Given:
# employees = ['Kelly', 'Emma']

# defaults = {"designation": 'Developer', "salary": 8000}
# Expected output:
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

# defaults.setdefault("salary", 8000)

def dict_with_default_values(keys_list, defaul_values):
    created_dictionary = {}

    for i in range(len(keys_list)):
        created_dictionary[keys_list[i]] = created_dictionary.setdefault(keys_list[i],
                                                                         {'designation': 'Developer', 'salary': 8000})
    return created_dictionary


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

assert dict_with_default_values(employees, defaults) == {'Kelly': {'designation': 'Developer', 'salary': 8000},
                                                         'Emma': {'designation': 'Developer',
                                                                  'salary': 8000}}, "Expected Outcome should be: {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}"


#   Delete a list of keys from a dictionary
# Given:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# Keys to remove
# keys = ["name", "salary"]
# Expected output:
# {'city': 'New york', 'age': 25}

def delete_list_of_keys(dict, keys_list):
    for i in dict.copy().keys():
        if i in keys_list:
            dict.pop(i)

    return dict


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

assert delete_list_of_keys(sample_dict, keys) == {'city': 'New york',
                                                  'age': 25}, "Expected Outcome should be: {'city': 'New york', 'age': 25}"

# Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.
# Write a Python program to check if value 200 exists in the following dictionary.
# Given:
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# Expected output:
# 200 present in a dict

sample_dict = {'a': 100, 'b': 200, 'c': 300}

# if 200 in sample_dict.values():
#   print('200 present in a dict')

#  Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.
# Given:
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# Expected output:
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict["location"] = sample_dict.pop("city")

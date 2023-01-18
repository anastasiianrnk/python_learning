# Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# Expected output:
# Math

def key_of_min_value(sample_dict):

  min_value = min(sample_dict.values())
  list_keys = []

  for key, value in sample_dict.items():
    if value == min_value:
      list_keys.append(key)

  return list_keys

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

assert key_of_min_value(sample_dict) == ['Math'], "Output Value should be [65]"

# Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
# Given:
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
# Expected output:
# {
#    'emp1': {'name': 'Jhon', 'salary': 7500},
#    'emp2': {'name': 'Emma', 'salary': 8000},
#    'emp3': {'name': 'Brad', 'salary': 8500}
# }

sample_dict['emp3']['salary'] = 8500
# print(sample_dict)

# Add a list of elements to a set
# Given a Python list, Write a program to add all its elements into a given set.
# Given:
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
# Expected output:
# Note: Set is unordered.
# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

def list_with_new_elements(sample_set, sample_list):

  for i in sample_list:
    sample_set.add(i)

  return sample_set

assert list_with_new_elements(sample_set, sample_list) == {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}, "Output Value should be {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}"

# Return a new set of identical items from two sets
# Given:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Expected output:
# {40, 50, 30}

def intersection_set(set1, set2):

  intersection_set = set1.intersection(set2)
  return intersection_set

assert intersection_set(set1, set2) == {40, 50, 30}, "Output Value should be: {40, 50, 30}"

# Get Only unique items from two sets
# Write a Python program to return a new set with unique items from both sets by removing duplicates.
# Given:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Expected output:
# {70, 40, 10, 50, 20, 60, 30}
# Note: set is unordered, so not necessary this will be the order of the item.

def union_set(set1, set2):

  union_set = set1.union(set2)
  return union_set

assert union_set(set1, set2) == {70, 40, 10, 50, 20, 60, 30}, "Output Value should be: {70, 40, 10, 50, 20, 60, 30}"

# Update the first set with items that don’t exist in the second set
# Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
# Given:
set1 = {10, 20, 30}
set2 = {20, 40, 50}
# Expected output:
# set1 {10, 30}

def difference_set(set1, set2):

  difference_set = set1.difference(set2)
  return difference_set

assert difference_set(set1, set2) == {10, 30}, "Output Value should be: {10, 30}"

# Remove items from the set at once
# Write a Python program to remove items 10, 20, 30 from the following set at once.
# Given:
set1 = {10, 20, 30, 40, 50}
# Expected output:
# {40, 50}

def remove_items_from_set(set1, list_to_remove):

  set_to_remove = set(list_to_remove)
  updated_set = set1.difference(set_to_remove)
  return updated_set

list_to_remove = [10, 20, 30]

assert remove_items_from_set(set1, list_to_remove) == {40, 50}, "Output Value should be: {40, 50}"

# Check if two sets have any elements in common. If yes, display the common elements
# Given:
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
# Expected output:
# Two sets have items in common
# {10}

def common_elements_set(set1, set2):

  intersection_set = set1.intersection(set2)
  return intersection_set

assert common_elements_set(set1, set2) == {10}, "Output Value should be: {10}"

# Remove items from set1 that are not common to both set1 and set2
# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {40, 50, 30}

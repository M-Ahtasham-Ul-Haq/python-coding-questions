"""
📘 Python Practice: Lists and Dictionaries
This file contains 12 essential questions and solutions related to Python lists and dictionaries.
Each function is defined with clear naming and sample usage for clarity.
"""

# 1. ✅ Find the second largest number in a list
def second_largest(numbers):
    unique = list(set(numbers))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

# 2. ✅ Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# 3. ✅ Count frequency of each item in a list using dictionary
def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# 4. ✅ Merge two dictionaries
def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

# 5. ✅ Sort a list in descending order
def sort_descending(lst):
    return sorted(lst, reverse=True)

# 6. ✅ Reverse a list using slicing
def reverse_list(lst):
    return lst[::-1]

# 7. ✅ Find common elements in two lists
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# 8. ✅ Find all even numbers in a list
def find_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# 9. ✅ Remove all odd numbers from a list
def remove_odd_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# 10. ✅ Convert list of tuples into dictionary
def tuples_to_dict(tuples):
    return dict(tuples)

# 11. ✅ Check if a key exists in a dictionary
def key_exists(d, key):
    return key in d

# 12. ✅ Find the item with the maximum value in a dictionary
def max_value_item(d):
    if not d:
        return None
    return max(d.items(), key=lambda x: x[1])

# === Example Usage (Testing) ===
if __name__ == "__main__":
    numbers = [5, 3, 9, 3, 7, 9, 2]
    print("Second Largest:", second_largest(numbers))
    print("Remove Duplicates:", remove_duplicates(numbers))
    print("Frequencies:", count_frequency(numbers))

    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 5, "c": 7}
    print("Merged Dicts:", merge_dicts(dict1, dict2))

    print("Sorted Descending:", sort_descending(numbers))
    print("Reversed List:", reverse_list(numbers))

    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    print("Common Elements:", find_common_elements(list1, list2))

    print("Even Numbers:", find_even_numbers(numbers))
    print("No Odd Numbers:", remove_odd_numbers(numbers))

    tuple_list = [("name", "Alice"), ("age", 25)]
    print("Dict from Tuples:", tuples_to_dict(tuple_list))

    sample_dict = {"apple": 50, "banana": 75, "cherry": 30}
    print("Key Exists (banana):", key_exists(sample_dict, "banana"))
    print("Max Value Item:", max_value_item(sample_dict))

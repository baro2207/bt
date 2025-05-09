'''to create a tuple of numbers and print one item.
 to unpack a tuple into several variables.
 to add an item to a tuple.
 to find the index of an item in a tuple.
 to find the repeated items of a tuple'''
from collections import Counter

def tuple_1():
    tpl = (1, 2, 4, 4, 5, 6, 6, 6, 9)
    for item in tpl:
        print(item)
    (a, b, *c) = tpl
    print(a, b, c)
    lst = list(tpl)
    lst.append(10)
    tpl = tuple(lst)
    print(tpl)
    index = 2
    for item in tpl:
        if item == index:
            print(item)
    counts = Counter(tpl)
    repeated = [item for item, count in counts.items() if count > 1]
    print("repeated items: ", repeated)

'''Write a Python program to find the maximum and minimum values in a set.
Write a Python program to check if a given value is present in a set or not.
Write a Python program to check if two given sets have no elements in common.
Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.'''

def set_1():
    set1 = {3, 6, 5, 7, 2, 1}
    print('max: ', max(set1))
    print('min: ',min(set1))

    value = 4
    print( value in set1 )

    set2 = {2, 8, 10, 1}
    print('no common elements: ', set1.isdisjoint(set2))

    def word_frequencies(strings):
        all_words = " ".join(strings).split()
        unique_words = set(all_words)
        for word in unique_words:
            print(f"{word}: {all_words.count(word)}")

    strings = ["hello world", "hello again", "world of python", "python hello"]

    word_frequencies(strings)

    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1

    print("Missing in second set (set1 - set2):", missing_in_set2)
    print("Missing in first set (set2 - set1):", missing_in_set1)

def dict_1():
#Convert two lists into a dictionary
    def dict_a():
        keys = ['name', 'age', 'city']
        values = ['Alice', 25, 'Hanoi']
        sampleDict = dict(zip(keys, values))
        print('Dict: ', sampleDict)

#Merge two Python dictionaries into one
    def dict_b():
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        merged_dict = dict1 | dict2
        print('merged 2 dict: ', merged_dict)

#Print the value of key ‘history’ from the below dict
    def dict_c():
        sampleDict = {
            "class": {
                "student": {
                    "name": "Mike",
                    "marks": {
                        "math": 90,
                        "history": 85
                    }
                }
            }
        }
        print("History: ", sampleDict["class"]["student"]["marks"]["history"])

#Initialize dictionary with default values
    def dict_d():
        employees = ['Alice', 'Bob', 'Charlie']
        defaults = {'designation': 'Developer', 'salary': 5000}
        new_dict = dict.fromkeys(employees, defaults)
        print("Dictionary with default values: ", new_dict)

#Create a dictionary by extracting the keys from a given dictionary
    def dict_e():
        original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        keys = ['a', 'c']
        new_dict = {k: original[k] for k in keys}
        print("Dict: ", new_dict)

#Delete a list of keys from a dictionary
    def dict_f():
        sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        keys_to_remove = ['a', 'c']
        for k in keys_to_remove:
            sample_dict.pop(k, None)
        print("Dict: ", sample_dict)

#Check if a value exists in a dictionary
    def dict_g():
        sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        values_to_check = 4
        if values_to_check in sample_dict.values():
            print('value exists:', values_to_check)
        else:
            print('value does not exist:', values_to_check)

#Rename key of a dictionary
    def dict_h():
        sampleDict = {'name': 'Alice', 'age': 25}
        sampleDict['full_name'] = sampleDict.pop('name')
        print("After rename: ", sampleDict)

#Get the key of a minimum value from the following dictionary
    def dict_i():
        sample_dict = {'a': 30, 'b': 10, 'c': 20}    
        min_key = min(sample_dict, key=sample_dict.get)
        print("Min values key: ", min_key)

# Change value of a key in a nested dictionary
    def dict_j():
        people = {'person': {'name': 'Alice', 'age': 25}}
        people['person']['age'] = 30
        print(people)

#Counts the number of times characters appear in a text paragraph.
    def dict_k():
        text = "Hello world! Python is great."
        char_count = {}
        for char in text:
            if char.isalpha():
                char = char.lower()
                char_count[char] = char_count.get(char, 0) + 1
        print(char_count)

#Using a dictionary containing keys starting from 1 and values containing prime numbers less than a value N.
    def dict_l():

        def is_prime(n):
            if n < 2: return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0: return False
            return True
        N = 20
        primes = [i for i in range(2, N) if is_prime(i)]
        prime_dict = {i + 1: prime for i, prime in enumerate(primes)}
        print("Từ điển số nguyên tố:", prime_dict)
def company():
    employees = {
        1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
        1002: {"name": "Bob", "department": "Sales", "salary": 50000},
        1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
        1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
        1005: {"name": "Eve", "department": "Sales", "salary": 55000}
    }
    dept_employees = {}
    for emp_id, info in employees.items():
        dept = info["department"]
        emp_info = {"name": info["name"], "salary": info["salary"]}

        if dept not in dept_employees:
            dept_employees[dept] = {}

        dept_employees[dept][emp_id] = emp_info
    print(dept_employees)

if __name__ == '__main__':
    company()
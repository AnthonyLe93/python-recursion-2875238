"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def iterative_str_len(a_str):
    j = 0
    for i in a_str:
        j += 1
    return j


def recursive_str_len(a_str):
    if a_str == '':
        return 0
    else:
        return 1 + recursive_str_len(a_str[1:])


input_str = "I love recursion"
assert iterative_str_len(input_str) == len(input_str)  # Standard Pythonic way
assert iterative_str_len(input_str) == recursive_str_len(input_str)

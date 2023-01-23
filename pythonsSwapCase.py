"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

"""

def swap_case(s):
    swappedCaseString = ''

    for i in s:
        if i.isupper():
            swappedCaseString += i.lower()
        elif i.islower():
            swappedCaseString += i.upper()
        else:
            swappedCaseString += i
    return swappedCaseString


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
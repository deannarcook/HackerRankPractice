"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
"""


def count_substring(string, sub_string):
    substringLength = len(sub_string)
    indexStart = 0
    indexEnd = substringLength
    substringCount = 0
    for i in string:
        if string[indexStart:indexEnd] == sub_string:
            substringCount += 1
        indexStart += 1
        indexEnd += 1

    return substringCount


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
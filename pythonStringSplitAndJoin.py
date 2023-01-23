"""
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""

def split_and_join(line):
    splitString = line.split(' ')
    returnString = "-".join(splitString)
    return returnString
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
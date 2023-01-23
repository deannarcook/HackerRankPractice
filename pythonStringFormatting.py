"""
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.
"""


def print_formatted(number):
    i = 1
    padding = len(str(bin(n)).replace('0b', ''))
    while i <= n:
        octal = str(oct(i)).replace('0o', '')
        hexidecimal = str(hex(i)).replace('0x', '')
        binary = str(bin(i)).replace('0b', '')
        print(str(i).rjust(padding, ' ') + ' ' + str(octal).rjust(padding, ' ') + ' ' + str(hexidecimal).rjust(padding,' ').upper() + ' ' + str(binary).rjust(padding, ' '))
        i += 1

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
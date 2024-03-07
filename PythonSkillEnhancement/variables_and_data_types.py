
# ~x (Bitwise NOT) operator
# The ~x operator inverts the bits of x. It is equivalent to -x - 1.
# For example, if x is 10, then ~x is -11.
# The result of ~x is always -(x + 1).
# The ~x operator is often used to create the two's complement of a number.
# The two's complement of a number is used to represent negative numbers in binary.
#
# Define an integer
x = 10  # In binary: 1010

# Invert the bits of x
inverted_x = ~x  # This will be -11 in decimal

# Explanation:
# The binary representation of 10 is 0000 1010 in 8 bits (for simplicity)
# After inverting: 1111 0101
# In two's complement (used for representing signed integers), this represents -11

print(f"Original x: {x} (binary: {bin(x)})")
print(f"Inverted ~x: {inverted_x} (binary: {bin(inverted_x)})")


# Text
# 'doesn\'t'  # use \' to escape the single quote...
# "doesn't"  # ...or use double quotes instead
# '"Isn\'t," they said.'
s = 'First line.\nSecond line.'  # \n means newline
# s  # without print(), special characters are included in the string
# 'First line.\nSecond line.'
print(s)  # with print(), special characters are interpreted, so \n produces new line
# First line.
# Second line.

# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print('C:\some\name')  # here \n means newline!
# C:\some
# ame
print(r'C:\some\name')  # note the r before the quote
# C:\some\name


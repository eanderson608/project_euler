# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#

def is_double_palindromic(x):

    return str(x) == str(x)[::-1] and str(bin(x)[2:]) == str(bin(x))[:1:-1]


result = [i for i in range(1000000) if is_double_palindromic(i)]
print result
print "sum : ", sum(result)

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# returns boolean indicating whether a multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
def mmp_pandigital(multiplicand, multiplier):

    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    product = str(multiplier * multiplicand)
    multiplier = str(multiplier)
    multiplicand = str(multiplicand)

    return  sorted(multiplicand + multiplier + product) == digits

total = set([])
for i in range(5000):
    for j in range(i):
        if mmp_pandigital(i, j):
            print i, j, i * j
            total.add(i * j)

print "total:", total
print "sum:", sum(total)

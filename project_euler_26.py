# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import decimal
prec = 10000

decimal.getcontext().prec = prec

# returns whether all items in a list are the same
def all_same(l):

    first_item = l[0]
    for item in l:
        if item != first_item:
            return False

    return True

def reciprocal_cycles(num):

    # get decimal portion of number with last digit removed
    dec = str(num.split('.')[1][:-1])

    # return 0 if there are no reciprocal cycles (decimal is finite)
    if len(dec) < prec - 1:
        return 0

    # if second half of num is all the same number return 1
    if all_same(dec[len(dec) / 2 :]):
        return 1

    for i in range(1, len(dec)):
        if dec[-i:] == dec[-i - i: -i]:
            print d, i, dec[-i:], dec[-i - i: -i]
            return i

    return 0

max_cycles = 0
max_d = 0
for i in range(2,1000):

    one = decimal.Decimal(1)
    d = decimal.Decimal(i)
    num = format(one / d, '1.10000')

    num_cycles = reciprocal_cycles(num)

    if num_cycles > max_cycles:
        max_cycles = num_cycles
        max_d = i

print max_d, max_cycles

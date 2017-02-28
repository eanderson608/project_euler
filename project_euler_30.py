# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


# the highest possible 5th power sum of a number with 6 digits (6 * 9**5)
# since (7 * 9**5) is only six digits, the maximum possible number equal to the sum of the fifth power of its digits cannot exceed 6 digits

def sum_of_power_of_digits(num, power):
     return sum([int(i) ** power for i in list(str(num))])

max_num = 354294 # 6*(9**5)


result = [i for i in range(2, max_num + 1) if i == sum_of_power_of_digits(i, 5)]
print result, sum(result)

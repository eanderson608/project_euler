# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math

# returns list of a numbers divisors including 1 but excluding itself
def divisors(num):
    divisors = [1]

    if num < 2:
        return []

    # if number has a perfect square, add it to divisor list
    if math.sqrt(num) % 1 == 0:
        divisors.append(int(math.sqrt(num)))

    for i in range(2, int(math.ceil(math.sqrt(num)))):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num / i)

    return sorted(divisors)

# generate list of booleans representing if each index is an abundant number
abundant_numbers = []
for i in range(28124):
    if sum(divisors(i)) > i:
        abundant_numbers.append(True)
    else:
        abundant_numbers.append(False)

# find numbers which cannot be written as the sum of two abundant numbers
result = []
for i in range(28124):

    sum_of_abundants = False
    for j in range(i + 1):
        if abundant_numbers[j] and abundant_numbers[i - j]:
            sum_of_abundants = True
            break
    if not sum_of_abundants:
        result.append(i)

print result, sum(result)

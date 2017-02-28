# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math

# returns list of a numbers divisors including 1 but excluding itself
def divisors(num):
    divisors = [1]

    if num < 2:
        return []

    # if number has a perfect square, add it to divisor list
    if math.sqrt(num) % 1 == 0:
        divisors.append(int(math.sqrt(num)))

    for i in range(2, int(math.floor(math.sqrt(num)))):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num / i)

    return sorted(divisors)

def d(num):
    return sum(divisors(num))

d_list = [0] # list to hold mapping of proper divisors (with a placeholder in 0th position since we dont need it)

# create list of proper divisors
for i in range(1,10000):
    d_list.append(d(i))

# test for amicable numbers
amicable_numbers = []
for i in range(1,10000):
    if d_list[i] < 10000 and i == d_list[d_list[i]] and d_list[d_list[i]] != d_list[i]:
        print i
        amicable_numbers.append(i)

print sum(amicable_numbers)

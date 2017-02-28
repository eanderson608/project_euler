# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find
# the product abc

import math

result = [(a, b) for a in range(1,500) for b in range(1, 500) if a < b and a + b + math.sqrt(a**2 + b**2) == 1000]

a, b = result[0]
c = math.sqrt(a**2 + b**2)
print a, b, c
print a*b*c

# Find the sum of the digits in the number 100!
import math

total = 0
for num in str(math.factorial(100)):
    total += int(num)

print total

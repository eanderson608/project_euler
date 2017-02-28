n = 1000 # 3 and 5 multiple cutoff
result = 0 # store running total

for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print result

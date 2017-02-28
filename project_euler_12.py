import math

tri = 0
nth_tri = 1
most_facs = 0

while True:
    tri = tri + nth_tri

    factors = []
    rounded_square = int(math.floor(math.sqrt(tri)))
    for i in range(1, rounded_square + 1):
        if tri % i == 0:
            factors.append(tri / i)
            if not math.sqrt(tri) == i:
                factors.append(i)

    if len(factors) > most_facs:
        most_facs = len(factors)
        print most_facs

    if len(factors) > 500:
        print nth_tri, tri, factors
        print "done"
        break
    nth_tri += 1

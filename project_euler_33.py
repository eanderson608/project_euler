# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# find all non-trivial numerator and denominators for problem
fractions = [(i, j, list(set(str(i)).intersection(set(str(j))))) for i in range(10,100) for j in range(10, i) if i % 10 != 0 and j % 10 != 0]

for fraction in fractions:
    d, n, common_term = fraction
    for term in common_term:
        new_n, new_d = list(str(n)), list(str(d))
        if term in new_n and term in new_d:
            new_n.remove(term)
            new_d.remove(term)
            new_n = float(new_n[0])
            new_d = float(new_d[0])

            if float(n) / float(d) == new_n / new_d:
                print new_n, new_d

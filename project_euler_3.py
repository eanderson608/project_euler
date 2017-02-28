n = 600851475143
prime_factor_list = [n]

# find prime factor
for pf in prime_factor_list:

    for i in xrange(2, pf):

        if pf % i == 0:
            prime_factor_list.remove(pf)
            prime_factor_list.append(i)
            prime_factor_list.append(pf / i)
            print prime_factor_list
            break

print "done"

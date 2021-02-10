
# print sum(1 for w in open('english.txt').read().splitlines() if w == w[::-1])  

# print sum(1 for w in open('/users/abrick/resources/english').read().splitlines() if w == w[::-1])

# print len(filter(lambda w: w == w[::-1], open('english.txt').read().splitlines()))

print len(filter(lambda w: w == w[::-1], open('/users/abrick/resources/english').read().splitlines()))


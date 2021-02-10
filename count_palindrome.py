# Option 1:

# To test locally:

# print sum(1 for word in open('english.txt').read().splitlines() if word == word.lower()[::-1])  

# To test in hills:

# print sum(1 for word in open('/users/abrick/resources/english').read().splitlines() if word == word.lower()[::-1])

# Option 2:

# To test locally:

# print len(filter(lambda word: word == word.lower()[::-1], open('english.txt').read().splitlines()))

# To test in hills:

print len(filter(lambda word: word == word.lower()[::-1], open('/users/abrick/resources/english').read().splitlines()))

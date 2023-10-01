#Counter

from collections import Counter

l = [1,1,1,1,1,2,3,4,5,5,5,6,7,8,8,8,9]

print(Counter(l))


s = 'How many times does each word shows up ? word word'
words = s.split()
print(Counter(words))

c = Counter(words)
print(c.most_common(2))



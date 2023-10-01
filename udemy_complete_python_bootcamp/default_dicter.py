from collections import defaultdict

d = {'key':1}


print(d['key'])
# print(d['k2'])


d = defaultdict(object)
print(d['one'])

for item in d:
    print(item)
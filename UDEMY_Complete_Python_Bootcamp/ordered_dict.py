d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['e'] = 5
d['d'] = 4
d['f'] = 6

print(d)

print('\n\n')


for k,v in d.items():
    print(k,v)

print('\n\n')

from collections import OrderedDict
e = OrderedDict()

e['a'] = 1
e['b'] = 2
e['c'] = 3
e['e'] = 5
e['d'] = 4
e['f'] = 6

for a,b in e.items():
    print(a,b)
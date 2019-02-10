import timeit

#create a string 1 - 99

print("-".join(str(n) for n in range(150)))

#QUICK FACTORIAL REDUCE USED!
from functools import reduce
fact = 5
product = reduce((lambda x, y: x * y), [x for x in range(1,fact+1)])
print(product)
#GENERATORS IN PYTHON 3

def create_cubes(n):
    #result = list()
    for x in range(n):
        yield x**3
        #result.append(x**3)
    #return result


a = create_cubes(10)
print(a)
print("\n")

for x in create_cubes(10):
    print(x)

print("\n")



def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b


for i in gen_fibon(10):
    print(i)


print("\n")

a = gen_fibon(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#print(next(a))      THIS WILL OCCUR STOPITERATION EXCEPTION ERROR


print("\n")

s = 'hello'
for l in s:
    print(l)


#print(next(s))

print("\n")

s_it = iter(s)
print(next(s_it))
#FACTORIAL

def fact(n):
    return 1 if n < 1 else n * fact(n - 1)

f = fact(5)
print(f)
print('\n')

a = fact(-2)
print(a)
print('\n')


#FIBON
def fibon():
    a = 1
    b = 1
    while True:
        yield a
        a,b = b, a+b


fib = fibon()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


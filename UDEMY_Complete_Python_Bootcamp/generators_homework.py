def gen_squares(n):
    for x in range(n):
        yield x**2

a = gen_squares(10)
print(a)

for x in gen_squares(10):
    print(x)



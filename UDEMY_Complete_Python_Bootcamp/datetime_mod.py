import datetime

t = datetime.time(5,25,1)
print(t)
print(t.minute)

today = datetime.date.today()
print(today)
now = datetime.datetime.now()
print(now)

def fibonn():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

f = fibonn()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))



def fact(n):
    factt = 1
    for i in range(1, n+1):
        factt = factt * i
    return factt

a = fact(5)
print(a)



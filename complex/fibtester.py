import time

def fib(val):
    if val in [0,1]:
        return 1

    return fib(val-1) + fib(val-2)

def fibfast(val):
    a = 1
    b = 1

    for i in range (1, val):
        c = a + b

        a = b
        b = c

    return b


t1 = time.time()
print(fib(5))
print(fib(36))
print(f'elapsed: {time.time() - t1:.2f}s')

t1 = time.time()
print(fibfast(5))
print(fibfast(36))
print(fibfast(500))
print(f'elapsed: {time.time() - t1:.2f}s')
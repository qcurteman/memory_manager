def fib(n):
    if n <= 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib2(n):
    steps = 0
    a = 1
    b = 0
    if n <= 2:
        return 1
    while steps < n:
        a, b = b, a + b
        steps += 1
    return a

print(fib(100))
print(fib2(100))

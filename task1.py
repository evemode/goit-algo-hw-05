def caching_fibonacci():
    cache = [] #blank list to store numbers

    def fibonacci(n):
        if n <=0:
            return 0
        elif n ==1:
            return 1
        elif n not in cache:
            return fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))
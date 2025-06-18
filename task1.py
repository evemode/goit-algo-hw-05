def caching_fibonacci():
    cache = {} #blank list to store numbers

    def fibonacci(n):
        if n in cache:
            return cache[n]
        elif n <=0:
            result = 0
        elif n ==1:
            result = 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result #save result to cache
        return result
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))

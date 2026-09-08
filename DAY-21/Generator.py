'''
def reels():
    data = ['1..100', '2..200', '3..300', '4..400', '5..500']
    for item in data:
        yield item  

res = reels()

print(next(res))  # Output: 1..100
print(next(res))  # Output: 2..200
print(next(res))  # Output: 3..300
print(next(res))  # Output: 4..400
print(next(res))  # Output: 5..500

def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
res2 = countdown()
for i in res2:
    print(i)  # Output: 5, 4, 3, 2, 1

def factors(T):
    for i in range(1, T + 1):
        if T % i == 0:
            yield i
res3 = factors(12)
for factor in res3:
    print(factor, end='\t')  # Output: 1, 2, 3, 4, 6, 12
'''
def prime_nums(n):
    for num in range(2, n + 1):
        is_prime = True   
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
res4 = prime_nums(20)
for prime in res4:
    print(prime)  # Output: 2, 3, 5, 7, 11, 13, 17, 19    


def isPrime(n):
    for i in xrange(3, int(n/2), 2):
        if n%i == 0:
            return(False)
    return(True)

sum = 2
for i in xrange(3, 2000000, 2):
    if isPrime(i):
        print(i)
        sum += i

print(sum)

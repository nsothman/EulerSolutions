def primeSum(n):
    sum = 0
    sieve = [True] * n
    for i in range(2, n):
        if sieve[i]:
            sum += i
            for j in range(i*i, n, i):
                sieve[j] = False
    return sum

print primeSum(2000000)

j = 1
i = 1

def isPrime(n):
    for i in range(2, int(n/2)):
        if n%i == 0:
            return(False)
    return(True)

while i < 10001:
    j += 2
    if isPrime(j):
        i += 1
print(j)

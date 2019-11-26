n = 600851475143

maxPrime = 1
while n%2 == 0:
    n = n/2
    maxPrime = 2
for i in range(3, int(n**0.5 + 1), 2):
    while n%i == 0:
        n = n / i
        maxPrime = i
if n > 2:
    maxPrime = n
print(maxPrime)

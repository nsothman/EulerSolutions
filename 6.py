squareSum = 0
sum = 0
for i in range(1,101):
    print(i)
    squareSum += i**2
    sum += i
print(squareSum)
print(sum**2)
print(sum**2 - squareSum)

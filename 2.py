sum = 2
fibNum = 0
firstNum = 1
secNum = 2
while fibNum < 4000000:
    fibNum = firstNum + secNum
    print(fibNum)
    firstNum = secNum
    secNum = fibNum
    if fibNum%2 == 0:
        sum += fibNum
print(sum)

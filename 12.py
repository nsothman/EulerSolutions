triNums = []
triNums.append(1)
i = 1
x = 0

while x <= 500:
    triNums.append(triNums[i - 1] + i + 1)
    x = 2
    for j in xrange(2, int(triNums[i]**0.5 + 1)):
        if triNums[i]%j == 0 and j == int(triNums[i]**0.5):
            x += 1
        elif triNums[i]%j == 0:
            x += 2

print(triNums[-1])

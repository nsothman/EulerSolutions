import os
import os.path

numFile = open("C:\\Users\\Anas Othman\\Desktop\\Coding\\Euler Solutions\\13 Numbers.txt")
num = 0
sum = 0

for i in range(100):
    num = int(numFile.readline())
    sum += num

print(str(sum)[0: 10])

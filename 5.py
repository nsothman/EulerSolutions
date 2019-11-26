i = 22
while True:
    Pass = True
    for j in range(1, 20):
        if i%j != 0:
            Pass = False
            break
    if Pass == True:
        print(i)
        break
    i += 2

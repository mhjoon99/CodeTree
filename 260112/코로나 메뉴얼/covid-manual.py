cnt = 0

for i in range(3):
    sym, temp = input().split()
    temp = int(temp)
    if sym=='Y' and temp>=37:
        cnt+=1

if cnt>=2:
    print('E')
else:
    print('N')

while True:
    a,b = map(int,input().split())
    counts_1 = 0
    counts_2 = 0
    if (a == 0 and b == 0) or a == b:
        break
    if a < b:
        for i in range(b):
            if a * i == b:
                print('factor')
                counts_1 += 1
                break
        if counts_1 == 0:
            print('neither')
    elif a > b:
        for i in range(a):
            if b * i == a:
                print('multiple')
                counts_2 += 1
                break
        if counts_2 == 0:
            print('neither')
'''
while True:
    a,b = map(int,input().split())
    if a==b==0:
        break
    if a%b==0:
        print('multiple')
    elif b%a==0:
        print('factor')
    else:
        print('neither')
'''
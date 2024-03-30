test = int(input())
for i in range(test):
    a = []
    times,string = input().split()
    for k in string:
        a.append(k*int(times))
    for i in a:
        print(i,end='')
    print()
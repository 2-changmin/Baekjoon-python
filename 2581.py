import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
prime_num_list = []
for i in range(m,n+1):
    a = []
    for k in range(1,i//2+1):
        if i % k == 0:
            a.append(k)
    if len(a) == 1:
        prime_num_list.append(i)
if sum(prime_num_list) == 0:
    print(-1)
else:
    print(sum(prime_num_list))
    print(min(prime_num_list))

'''        
def so(a):
    if a==1:
        return False
    else:
        for i in range(2,a):
            if a%i==0:
                return False
        return True

m = int(input())
n = int(input())
list = []
for i in range(m,n+1):
    if so(i) is True:
        list.append(i)
if list == []:
    print(-1)
else:
    print(sum(list))
    print(min(list))
'''
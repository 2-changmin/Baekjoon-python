import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = [i for i in range(1,n+1)]
for k in range(m):
    i,j = map(int,input().split())
    b = a[i-1:j]    #왜 j는 j-1 이 아닌지 - 역순 해야하는 부분을 슬라이싱 해줘야 하는데 j-1로 슬라이싱하면 j는 포함되지 않기때문
    b.reverse()
    a[i-1:j] = b

for i in range(n):
    print(a[i],end=' ')
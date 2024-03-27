import sys
input = sys.stdin.readline
n,x=input().split()
n,x=int(n),int(x)
a_list = list(map(int,input().split()))
for i in a_list:
    if i<x:
        print(i,end=' ')
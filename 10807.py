n = int(input())
a = input()
a = a.split()
v = input()
x = 0
for i in a:
    if i == v:
        x += 1
print(x)

'''a= int(input())
b=list(map(int,input().split()))
c=int(input())
print(b.count(c))'''
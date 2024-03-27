'''a = 0
c = 0
for i in range(1,10):
    b = int(input())
    if b>a:
        a = b
        c = i
print(a)
print(c)'''

list = []
for i in range(9):
    list.append(int(input()))

m = max(list)
print(m)
print(list.index(m)+1)
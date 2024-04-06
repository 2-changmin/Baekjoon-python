a = []
max_list = []
time = 0
#5~6 번 코드를 arr = [list(map(int,input().split())) for _ in range(9)] 이렇게 간단히 작성 가능
for i in range(9):
    i = list(map(int,input().split()))
    a.append(i)
    b = max(i)
    max_list.append(b)
c = max(max_list)
print(c)
for i in a:
    time += 1
    if c in i:
        d = i.index(c)
        print(time,d+1)
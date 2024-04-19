n = int(input())
result = 0
for i in range(1, n+1):
    a = list(map(int,str(i)))  # ex) 215 = [2, 1, 5]
    s = i + sum(a)  # s = 생성자
    if s == n:
        result = i
        break
print(result)
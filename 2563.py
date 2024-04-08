white_paper = [[0 for j in range(100)] for i in range(100)]
counts = 0

n = int(input())

for i in range(n):
    x, y = list(map(int, input().split()))
    
    for x_idx in range(x,x+10):
        for y_idx in range(y, y+10):
            white_paper[x_idx][y_idx] = 1

for i in white_paper:
    counts += i.count(1)
'''
for i in range(100):
    for j in range(100):
        counts+=white_paper[i][j]
print(counts)    이렇게 작성해도 됨 because 어차피 도화지가 안 붙여진 부분은 0이고 붙여진 부분만 1이라서 다 더하면 넓이가 나오기 때문
'''
print(counts)
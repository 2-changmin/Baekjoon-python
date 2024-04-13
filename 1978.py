''' 처음 작성한 코드
n = int(input())
a = list(map(int,input().split()))
sot_num = 0
for i in a:
    b = []
    if i == 1:
        continue
    for k in range(1,i+1):
        if i%k==0:
            b.append(k)
    if len(b) == 2:
        sot_num += 1
print(sot_num)
'''
#수정 조금 더 깔끔하게 코드 작성할 수 있을 것 같음 ->
#달라진 점은 처음 작성한 코드의 7~8 부분이 굳이 들어가지 않아도 될 거라고 판단해서 제외했음
n = int(input())
a = list(map(int,input().split()))
counts = 0
for i in a:
    b = []
    for k in range(1,i+1):
        if i%k==0:
            b.append(k)
    if len(b) == 2:
        counts += 1
print(counts)

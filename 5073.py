while True:
    a,b,c = map(int,input().split())
    if a==b==c==0:
        break
    if max([a,b,c]) >= sum([a,b,c]) - max([a,b,c]):
        print('Invalid')
    elif a==b==c:
        print('Equilateral')
    elif a==b or a==c or b==c:
        print('Isosceles')
    else:
        print('Scalene')

'''
while True:
    arr = list(map(int,input().split()))
    if sum(arr) == 0:
        break
    else:
        arr = sorted(arr)  #arr리스트를 오름차순으로 재배열
        print(['Invalid','Equilateral','Isosceles','Scalene'][int(arr[-1]<sum(arr[:-1]))*len(set(arr))])
        #'arr[-1]<sum(arr[:-1])' : 가장 긴 변이 나머지 두 변의 길이의 합보다 작은지 비교
        #'int(arr[-1]<sum(arr[:-1]))' : 위의 비교 결과가 True 일 경우 1, False일 경우 0을 반환
        #'len(set(arr))' : 주어진 변의 길이들 중 서로 다른 길이의 수를 계산한다.
'''
n,k = map(int,input().split())
x = list(map(int,input().split()))
take_award = []
x.sort(reverse=True)
print(x[k-1])
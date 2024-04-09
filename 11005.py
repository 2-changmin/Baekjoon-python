n,b = map(int,input().split())
alpha_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_list = list(range(36))

result =''

while n >= b:
    idx = n % b
    
    alpha_idx = num_list.index(idx)
    result += alpha_list[alpha_idx]
    
    n = n // b
    
alpha_idx = num_list.index(n)
result += alpha_list[alpha_idx]

print(result[::-1])

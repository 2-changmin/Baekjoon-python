n = int(input())
count = 0
for i in range(n):
    text = input()
    a = []
    a.append(text[0])
    check = True
    
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            pass
        elif text[i] != text[i+1]:
            if text[i+1] in a:
                check = False
            a.append(text[i+1])
    if check == True:
        count += 1
print(count)
word = input().upper()
a = [0] * 26

for i in word:
    index = ord(i) - ord('A')
    a[index] += 1

max_count = max(a)
max_index = a.index(max_count)

if a.count(max_count) > 1:
    print("?")
else:
    print(chr(max_index + ord('A')))
    
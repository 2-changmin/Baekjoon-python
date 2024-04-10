n = int(input())

end_num = 1
start_num = 1
room = 1
add_1 = 6
add_2 = 6

while end_num < n:
    if n == 1:
        break
    end_num += add_1
    add_1 += add_2
    room += 1

print(room)

'''
n = int(input())
house = 1
count = 1

while n > house:
    house += 6 * count
    count += 1
print(count)
'''
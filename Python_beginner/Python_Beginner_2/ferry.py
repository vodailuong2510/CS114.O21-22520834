import sys
l, m = map(int, sys.stdin.readline().split())

cars_at_left = []
cars_at_right = []
for _ in range(m):
    data = sys.stdin.readline().split()
    if data[1] == 'left':
        cars_at_left.append(int(data[0]))
    else:
        cars_at_right.append(int(data[0]))

turns = 0
i_left = [0]
i_right = [0]
while len(i_left) + len(i_right) - 2 < m:
    remain_length = l * 100
    if turns % 2 == 0:
        for i in range(i_left[-1], len(cars_at_left)):
            if remain_length - cars_at_left[i] >= 0 :
                remain_length -= cars_at_left[i]
                i_left.append(i+1)
            else:
                break
    else:
        for i in range(i_right[-1], len(cars_at_right)):
            if remain_length - cars_at_right[i] >= 0:
                remain_length -= cars_at_right[i]
                i_right.append(i+1)
            else:
                break
    turns += 1
print(turns)
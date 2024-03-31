import sys
n = int(sys.stdin.readline())

def direction(A, B):
    x1, y1 = A
    x2, y2 = B

    if x1 == x2:
        return "^" if y2 > y1 else "V"
    else:
        return ">" if x2 > x1 else "<"

def count_right_turns(n, points):
    right_turns = 0
    for i in range(n-2):
        current_point = points[i]
        next_point = points[i+1]
        after_next_point = points[i+2]
        
        current_direction = direction(current_point, next_point)
        next_direction = direction(next_point, after_next_point)

        if current_direction == "^" and next_direction == ">":
            right_turns += 1
        elif current_direction == ">" and next_direction == "V":
            right_turns += 1
        elif current_direction == "V" and next_direction == "<":
            right_turns += 1
        elif current_direction == "<" and next_direction == "^":
            right_turns += 1
    
    print(right_turns)
points = []
for i in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))

count_right_turns(n, points)

import sys
n = int(sys.stdin.readline())
time_bristle = [float(i) for i in sys.stdin.readline().split()]
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
z = float(sys.stdin.readline())

end_time = [i + z for i in time_bristle]
dame = 0
end_time_ = 0
gai = 0
for i in time_bristle:
    if i < end_time[end_time_]:
        dame += x + gai * y
        gai += 1
    elif i == end_time[end_time_]:
        dame += x + gai * y
        end_time_ += 1
    else:
        step = 0
        while i > end_time[end_time_] and end_time_ <= n-1:
            end_time_ += 1
            step += 1
        gai -= step
        dame += x + gai * y
        gai += 1

print(dame)
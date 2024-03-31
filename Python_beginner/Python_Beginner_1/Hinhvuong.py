import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# Tính vectơ AB
AB = [B[0] - A[0], B[1] - A[1]]

AC = [-1 * AB[1], AB[0]]

# Tính tọa độ điểm C và D
C1, D1= [B[0] + AC[0], B[1] + AC[1]], [A[0] + AC[0], A[1] + AC[1]]
C2, D2 = [B[0] - AC[0], B[1] - AC[1]], [A[0] - AC[0], A[1] - AC[1]]

print(f"({A[0]}, {A[1]}) ({D1[0]}, {D1[1]}) ({C1[0]}, {C1[1]}) ({B[0]}, {B[1]})")
print(f"({A[0]}, {A[1]}) ({B[0]}, {B[1]}) ({C2[0]}, {C2[1]}) ({D2[0]}, {D2[1]})")

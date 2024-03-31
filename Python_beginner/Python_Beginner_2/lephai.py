import sys
def xuat_mang_canh_le_phai(arr):
    max_lengths = tuple(max(len(str(row[i])) for row in arr) for i in range(len(arr[0])))
    
    for row in arr:
        print(' '.join(str(row[i]).rjust(max_lengths[i]) for i in range(len(row))))

r, c = map(int, sys.stdin.readline().split())
matrix = tuple(sys.stdin.readline().split() for _ in range(r))
xuat_mang_canh_le_phai(matrix)

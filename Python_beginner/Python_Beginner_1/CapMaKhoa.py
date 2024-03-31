import sys
L, R = map(int, sys.stdin.readline().split())
    
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def is_special_number(num):
    if int(num**0.5)**2 == num or num % 4 == 0 or num % 9 == 0:
        return 0
    
    sqrt_num = int(num**0.5) + 1
    for i in range(5, sqrt_num,6):
        if num % i == 0 and (num % i**2 == 0 or int((num / i) ** 0.5) ** 2 == num / i):
                return 0
        elif num % (i + 2) == 0 and ((num % (i + 2)**2 == 0 or int((num / (i + 2)) ** 0.5) ** 2 == num / (i + 2))):
          return 0
    return 1

R = R + 1
if L == 1:
    selected_numbers = [1]
    for i in range(L + 1, R):
        if is_special_number(i):
            selected_numbers.append(i)
else:
    selected_numbers = list(i for i in range(L, R) if is_special_number(i))

num_ways = 0
length = len(selected_numbers)
for i in range(length):
    for j in range(i+1, length):
        num_1, num_2 = selected_numbers[i], selected_numbers[j]
        if num_2 % num_1 == 0 and num_1  != 1:
            continue
        if gcd(num_1, num_2) == 1:
            num_ways += 1

sys.stdout.write(str(num_ways))
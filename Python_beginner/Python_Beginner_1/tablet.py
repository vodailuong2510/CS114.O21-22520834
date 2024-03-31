size = int(input())

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return divisors

divisors = find_divisors(size)
divisors.sort()

num_ways = 0
triplets = []
for c in divisors:
    for m in range(1, int(c**0.5) + 1):
        n = (c - m**2)**0.5
        if n <= 0 or n >= m:
            continue
        a = m**2 - n**2
        b = 2*m*n
        if int(b) == b and (a, b, c) not in triplets and (b, a, c) not in triplets:
            b = int(b)
            yes = True
            for triplet in triplets:
                ai, bi, ci = triplet
                k = c/ci
                if ((b / ai == k and a / bi == k) or (a / ai == k and b / bi == k)):
                    yes = False
                    break
            if yes == True:
                num_ways += 1
                triplets.append([a,b,c])
print(num_ways)

    

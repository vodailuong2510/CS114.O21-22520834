num_test = int(input())

def same_characters(a, b):
    a , b = list(a), list(b)
    char_count_a = {}
    char_count_b = {}
    for index in range(len(a)):
        if a[index] not in b:
            return 0
        char_count_a[a[index]] = char_count_a.get(a[index], 0) + 1
        char_count_b[b[index]] = char_count_b.get(b[index], 0) + 1
    for char in a:
        if char_count_a[char] != char_count_b.get(char, 0):
            return 0
    return 1

def same_characters_at_odd_index(a,b):
    a , b = list(a), list(b)
    char_count_a = {}
    char_count_b = {}
    for index in range(0,len(a),2):
        char_count_a[a[index]] = char_count_a.get(a[index], 0) + 1
    for index in range(0,len(b),2):
        char_count_b[b[index]] = char_count_b.get(b[index], 0) + 1
    for index in range(0,len(a),2):
        if char_count_a[a[index]] != char_count_b.get(a[index],0):
            return 0
    return 1
def reversed_substring(a,b):
    if a == b:
        return 1
    if len(a) != len(b) or len(a) < 3 or same_characters(a,b) == 0:
        return 0
    if same_characters_at_odd_index(a,b) == 1:
        return 1
    return 0
for i in range(num_test):
    a = input()
    b = input()
    if reversed_substring(a,b) == 1:
        print("YES")
    else:
        print("NO")
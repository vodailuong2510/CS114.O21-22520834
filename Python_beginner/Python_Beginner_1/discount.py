import re
prices = input().split()
prices = [float(x) for x in prices]

discounts = []
percentages = [0]
numbers = [1,2,3,4,5,6,7,8,9]
online = []
in_store = []
for i in range(len(prices)):
    discount = input()
    discounts.append(discount)
    match = re.search(r'\b\d+(\.\d+)?\b', discount)
    if match:
        percentages.append(match.group())
    else:
        percentages.append(0)
    if 'higher than in-store' in discount:
        in_store.append(i+1)
        online.append(0)
    else:
        online.append(i+1)
        in_store.append(0)

money = float(input())
percentages = [float(x) for x in percentages]

online_total = 0
in_store_total = 0

for i in range(len(prices)):
    online_total += prices[i] - prices[i] * percentages[online[i]]/100
    in_store_total += prices[i] - prices[i] * percentages[in_store[i]]/100

if money >= online_total or money >= in_store_total:
    print("true")
else:
    print("false")


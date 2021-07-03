n = int(input())
lst = []
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

answer = []
for x in lst:
    if (x % 2) == 0:
        answer.append(x)
    else:
        continue

print(sum(answer))
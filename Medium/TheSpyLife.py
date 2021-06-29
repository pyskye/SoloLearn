message = str(input())
answer = []

for x in message:
    if x.isalpha():
        answer.append(x)
    elif x == " ":
        answer.append(x)
    else:
        continue

answer.reverse()
spy = "".join(answer)
print(spy)

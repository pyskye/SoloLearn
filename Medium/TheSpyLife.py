message = str(input())
answer = []

for x in message:
    if (x>="a" and x<="z") or (x>="A" and x<="Z"):
        answer.append(x)
    elif x == " ":
        answer.append(x)
    else:
        continue

answer.reverse()
spy = "".join(answer)
print(spy)

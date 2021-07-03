text = str(input())
answer = []

for x in text:
    if x.isalnum():
        answer.append(x)
    elif x == " ":
        answer.append(x)
    else:
        continue

symbols = "".join(answer)
print(symbols)
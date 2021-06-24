point = int(input())
cost = int(input())

ticket = point // 12
if ticket >= cost:
    print("Buy it!")
else:
    print("Try again")
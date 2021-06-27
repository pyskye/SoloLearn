peso = int(input())
dollar = int(input())

exchange = peso*0.02
if dollar > exchange:
    print("Pesos")
elif dollar < exchange:
    print("Dollars")
else:
    print("Same")
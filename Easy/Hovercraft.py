sales = int(input())


profit = 3000000*sales - (1000000 + 2000000*10) 

if profit > 0:
    print("Profit")
elif profit < 0:
    print("Loss")
else:
    print("Broke Even")
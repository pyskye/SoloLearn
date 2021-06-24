txt = input()

x = txt.split()
print(max(x, key = len))

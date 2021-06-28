letters = str(input())

i = 0
for x in letters:
    if letters.count(x) > 1:
        i += 1

if i > 1:
    print("Deja Vu")
else:
    print("Unique")
 
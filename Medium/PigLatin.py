sentence = str(input())
word = sentence.split()

for x in word:
    print(x[1:] + x[0] + "ay", end=" ")
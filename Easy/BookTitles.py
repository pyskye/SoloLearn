file = open("/usercode/files/books.txt", "r")

lines = file.readlines()

for line in lines:
    if line[-1] == "\n":
        print("%s%i" % (line[0], (len(line)-1)))
    else:
        print("%s%i" % (line[0], len(line)))

file.close()

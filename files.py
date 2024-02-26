f = open("x files.txt", "a")
while True:
    line = input("gime me some text to put into the file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

#we need to cloe the file at the end
f.close()
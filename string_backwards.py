# iterate over a string backwards using while
text = "abcdefg"
i = -1
while i >= -7:
    print(text[i])
    i -= 1

# not complete:
text = "abcdefg"
i =0
while i < len(text):
    print(text[i])
    i +=1
#also
text = "abcdefg"
i =0
while i < len(text):
    print(text[len(text)-1-i])
    i +=1


text = input("Enter Text: ")
asc = "" 
leng = len(text)

for a in range (0,leng):
    char = ord(text[a])
    asc = asc + " " + str(char)

print(asc)
    

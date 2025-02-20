charList = []
for x in range(0, 5):
    char = input("Enter a character: ")[0]
    charList.append(char)

print("alphabetical: ", sorted(charList))
print("reversed: ", charList[::-1])

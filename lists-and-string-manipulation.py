charList = []
for x in range(0, 5):
    char = input("Enter a character: ")[0]
    charList.append(char)

print("alphabetical: ", sorted(charList))
print("reversed: ", charList[::-1])

print("____________________________")
print("name: John Hynes C. Longares")
print("student number: 20211121312")
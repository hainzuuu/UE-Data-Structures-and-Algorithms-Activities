A = set()
B = set()
C = set()

def inputset(set_letter, letter):
    print("SET:", letter)
    for x in range(0,5):
        set = int(input("Enter an integer: "))
        set_letter.add(set)

inputset(A, "A")
print("____________________")
inputset(B, "B")
print("____________________")
inputset(C, "C")
print("____________________")


print("Union of sets (A and C): ", A | C)
print("Intersection of sets (A and B): ", A & B)
print("Symmetric difference of sets (B and C): ", B ^ C)
print("____________________")
print("name: Longares, John Hynes C.")
print("student no.: 20211121312")



class stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.items) < 5:
            if item % 2 == 0:
                self.items.append(item)
            else:
                self.items.pop()

    def show(self, stack_number):
        print("s" + stack_number + ": ", end='')
        for x in self.items:
            print(x, end = ' ')
        print()

    def size(self):
        return len(self.items)

    def pop(self):
        self.items.pop()

s1 = stack()
s2 = stack()
s3 = stack()

number = None

def pop_all():
    s1.pop()
    s2.pop()
    s3.pop()

def pop2():
    try:
        pop_all()
        print("popping initiated")
    except IndexError:
        print("popping initiated")

while number != 0:
    number = int(input("Enter integer: "))
    if s1.size() < 5:
        if number % 2 == 0:
            s1.push(number)
        else:
            pop2()

    elif s1.size() > 4 and s2.size() < 5:
        if number % 2 == 0:
            s2.push(number)
        else:
            pop2()

    elif s2.size() > 4 and s3.size() < 5:
        if number % 2 == 0:
            s3.push(number)
        else:
            pop2()
    else:
        if number % 2 == 1:
            pop2()
        else:
            print("No space available, need to enter negative values")


    print("______________")
    s1.show("1")
    s2.show("2")
    s3.show("3")
    print("______________")

print("____________________")
print("name: Longares, John Hynes C.")
print("student no.: 20211121312")
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if len(item) == 1:
            self.items.insert(0, item)
        else:
            print("Input 1 character only.")

    def dequeue(self):
        try:
            self.items.pop()
        except IndexError:
            print("nothing to pop")

    def size(self):
        print(len(self.items))

    def display(self):
        print("queue: ", end='')
        for x in (self.items):
            print(x, end=", "
                         "")
        print()

    def count(self):
        vowel_count = 0
        vowels = 'aeiouAEIOU'
        for elements in self.items:
            if elements in vowels:
                vowel_count += 1
        print("Vowel count: ", vowel_count)


queue = Queue()

number = None

print("LEGEND:")
print("1 - Enqueue")
print("2 - Dequeue")
print("3 - Show queue size")
print("4 - Show all items")
print("5 - Show number of vowels")
print("6 - Exit the loop")
print("__________________________")

while number != 6:

    number = int(input("Enter number 1-6: "))
    if number == 1:
        char = input("Enter one character only: ")
        queue.enqueue(char)

    elif number == 2:
        queue.dequeue()

    elif number == 3:
        queue.size()

    elif number == 4:
        queue.display()

    elif number == 5:
        queue.count()

    elif number == 6:
        break

    else:
        print("Enter 1-6 only")


print("__________________________")
print("name: Longares, John Hynes C.")
print("student no.: 20211121312")
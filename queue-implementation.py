class Queue:
    def __init__(self):
        self.items = [] 

    def queue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        try:
            self.items.pop()
        except IndexError:
            print("nothing to pop")
    def size(self):
        return len(self.items)
        
    def showAll(self, order):
        print("q" + str(order) + ": ", end = "")
        for x in (self.items):
            
            print(x, end = " ")
        print()
        
q1 = Queue()
q2 = Queue()
q3 = Queue() 

def que3(number):
    if q3.size() < 5:
        q3.queue(number)
    else:
        q1.dequeue()
        q2.dequeue()
        
number = None 

while number != 0:
    number = int(input("Enter an integer: "))
    if number > 0:
        if number % 2 == 0:
            if q1.size() < 5:
                q1.queue(number)
            else:
                que3(number)
        else:
            if q2.size() < 5:
                q2.queue(number)
            else:
                que3(number)
    elif number < 0:
        q3.dequeue()
    
    q1.showAll(1)
    q2.showAll(2)
    q3.showAll(3)

print("____________________")
print("name: Longares, John Hynes C.")
print("student no.: 20211121312")
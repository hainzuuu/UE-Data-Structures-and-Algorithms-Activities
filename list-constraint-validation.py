int_list = []
temp_list = []

while len(int_list) < 10:
    num = int(input("enter integer: "))
    temp_list.append(num)
    if len(temp_list) < 3:
        int_list.append(num)
    if len(temp_list) > 2:
        if (temp_list[0] * temp_list[1] * temp_list[2]) % 2 == 1:
            print("You cannot enter 3 consecutive odd integers")
            del temp_list[-1]
        else:
            int_list.append(temp_list[2])
            if len(temp_list) == 3:
                del temp_list[0]

print("final: ", int_list)

print("____________________")
print("name: Longares, John Hynes C.")
print("student no.: 20211121312")

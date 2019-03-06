
our_items = ["T-shirt","Sweater"]
while True:
    Request = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if Request =="R":
        print(our_items)
    elif Request =="C":
        new_items = input("Enter new item: ")
        our_items.append(new_items)
        print(our_items)
    elif Request == 'U':
        up_pos = int(input("Update position? : "))
        update_item = input(" New item ? : ")
        if up_pos <= len(our_items):
            our_items[up_pos-1] = update_item
        else: 
            print("Position is invalid. Please try again!")
        print('Our items:',our_items)
    elif Request == 'D':
        del_pos = int(input("Delete position ? :"))
        if del_pos <= len(our_items):
            our_items.remove(our_items[del_pos-1])
        else: 
            print("Position is invalid. Please try again!")
        print(our_items)
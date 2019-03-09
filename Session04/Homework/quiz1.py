asw = {"1":35,"2":36,"3":40,"4":44}
while True:
    print("Answer the following algebra question:",end="")
    print("If x = 8, then what is the value of 4(x + 3)? ")
    for (k,v) in asw.items():
        print(k,v,sep=".")
    choose = input("your choice : ")
    if choose == "4":
        print("bingo ")
        break 
    else:
        print(":(")
        break



    



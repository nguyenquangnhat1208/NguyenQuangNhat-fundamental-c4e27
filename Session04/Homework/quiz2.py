asw1 = {"1":35,"2":36,"3":40,"4":44}
asw2 = {"1": "About 55","2": "About 65","3": "About 75","4": "About 85"}
question1 = ["Answer following algebra question:",
            "If x = 8, then what is the value of 4(x + 3)? "]
question2 = ["Estimated this answer", 
            "Jack score these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?"]
quiz = {"question": [question1, question2], "choice": [asw1, asw2],"answer":["4","2"] }
asw_list = []
asw_correct = 0
for i in range(2):
    print(*quiz["question"][i], sep = "\n")
    for (k,v) in quiz["choice"][i].items():
        print(k,v,sep = ". ")
    ur_asw = input("your choice :")
    if ur_asw == quiz["answer"][i]:
        print("bingo")
    else :
        print(":(")
    asw_list.append(ur_asw)  
    if asw_list[i] == quiz["answer"][i]:
        asw_correct = asw_correct + 1
print("your correctly answer",asw_correct,"out of 2 question")


    
def evaluate (a,b,operator):
    if operator=="*":
        return a*b 
    elif operator=="+":
        return a+b
    elif operator=="-":
        return a-b 
    else:
        return a/b 
x = evaluate(4,2,"/")
print(x)




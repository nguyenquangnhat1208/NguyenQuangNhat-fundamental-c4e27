import math 
a = int(input("Nhập vào hệ số a :"))
b = int(input("Nhập vào hệ số b :"))
c = int(input("Nhập vào hệ số c :"))
delta = b**2 - 4*a*c
if delta < 0:
    print("phương trình vô nghiệm")
elif delta == 0:    
    x = -b/2*a
    print("phương trình có nghiệm kép",x)
else:   
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("phương trình có 2 nghiệm",x1 , x2)

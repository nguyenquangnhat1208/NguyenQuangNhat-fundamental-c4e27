def add_two_number(a,b):
    return a+b
 
    # print("tổng 2 số là ",a+b)

num1 = int(input("nhap so thu nhat "))
num2 = int(input("nhap so thu hai "))
num3 = int(input("nhap so thu ba "))
num_1_2 = add_two_number(num1,num2)
num_3 = add_two_number(num_1_2,num3)
print("tong 3 so la ", num_3)
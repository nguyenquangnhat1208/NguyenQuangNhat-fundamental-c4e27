# yob = input("nhap nam sinh : ")
# if yob.isdigit()
#     age = 2019 - int(yob)
#     print("tuoi cua ban la : ",age)
# else:
#     print("nhập sai mời nhập lại ")
yob = input("nhap nam sinh : ")
while not yob.isdigit():
    print("bạn nhập sai rồi mời nhập lại")
    yob = input("nhap nam sinh :")
age = 2019 - int(yob)
print("tuoi cua ban la : ",age)


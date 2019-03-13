n = int(input("nhập vào n số : "))
tong = 0
for i in range(n):
    so = int(input("nhập vào số : "))
    # print("nhập vào số :",so)
    tong = tong + so 
print("tổng các số vừa nhập là",tong)
print("trung bình cộng các số vừa nhập là",tong/n)
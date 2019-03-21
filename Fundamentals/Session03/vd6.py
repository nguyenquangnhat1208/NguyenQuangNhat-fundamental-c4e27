# cho dãy n số nguyên tính tổng dãy vừa nhập vào , tính tổng các số lẻ , tính tổng các số chẵn , tính trung bình cộng các số chẵn
ls = []
n = int(input("moi ban nhap so phan tu:"))
for i in range(n):
    print("nhap phan tu thu: ",i)
    so = int(input(""))
    ls.append(so)
print("day ban vua nhap la:")
print(ls)

print("tong day vua nhap :")
print(sum(ls))

print("phan tu thu 2 trong day")
print(ls[1])

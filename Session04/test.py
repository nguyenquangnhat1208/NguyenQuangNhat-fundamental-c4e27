#tạo 1 danh sách in ra các cặp số có tổng là chẵn
ls = []
n = int(input("moi ban nhap so phan tu:"))
for i in range(n):
    print("nhap phan tu thu: ",i)
    so = int(input(""))
    ls.append(so)
print(ls)
for i in range(n):
    for j in range(i+1,n):
        if (ls[i]+ls[j])%2==0:
            print(ls[i],ls[j])

